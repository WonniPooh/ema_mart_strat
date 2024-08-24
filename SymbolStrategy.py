import json
import time
import secrets
import string
from datetime import datetime
from db_connector import db_new_finished_deal, db_insert_config, db_new_deal, db_new_finished_order
from PySide6.QtCore import QObject, Signal
from common import *
import bingx_api

LONG = 1
SHORT = -1

def generate_id(length):
    alphabet = string.ascii_letters + string.digits
    order_id = ''.join(secrets.choice(alphabet) for i in range(length))
    return order_id

def calculate_ema(data, span):
    if not data or span <= 0:
        return []

    ema_values = [data[0]]  # The first EMA value is the same as the first data point
    multiplier = 2 / (span + 1)

    for price in data[1:]:
        ema = (price - ema_values[-1]) * multiplier + ema_values[-1]
        ema_values.append(ema)

    return ema_values

def extend_ema(ema_values, price, span):
    multiplier = 2 / (span + 1)
    ema = (price - ema_values[-1]) * multiplier + ema_values[-1]
    ema_values.append(ema)


class DealReport:
    def __init__(self, symbol=None, timeframe="", direction="", leverage=1,
                 ts_start=0, ts_end=0, position_size=0.0, mart_steps=0,
                 total_result=0.0, commission=0.0):
        self.symbol = symbol
        self.timeframe = timeframe
        self.direction = direction
        self.leverage = leverage
        self.commission = commission
        self.total_position = position_size
        self.total_result = total_result
        self.mart_steps = mart_steps
        self.timestamp_start = ts_start
        self.timestamp_end = ts_end

    def get_by_index(self, index):
        if index == 0:
            return self.symbol
        if index == 1:
            return self.timeframe
        if index == 2:
            return self.direction
        if index == 3:
            return self.leverage
        if index == 4:
            return datetime.fromtimestamp(self.timestamp_start).strftime("%d.%m %H:%M:%S")
        if index == 5:
            return datetime.fromtimestamp(self.timestamp_end).strftime("%d.%m %H:%M:%S")
        if index == 6:
            return self.total_position
        if index == 7:
            return self.mart_steps - 1
        if index == 8:
            return self.total_result
        if index == 9:
            return round((self.total_result / self.total_position) * 100, 2)
        if index == 10:
            return self.commission


class SymbolStrategy(QObject):
    strat_status_updated = Signal(str, str)

    def __init__(self, cfg, manager, logger) -> None:
        super().__init__()
        self.manager = manager

        self.logger = logger
        self.cfg = cfg
        self.config_id = None

        self.symbol = self.cfg.symbol
        self.stopped = True
        self.is_updated = False #if position is active, but no klines updates allowed

        self.slow_ema = []
        self.fast_ema = []

        self.bars_delay = 0
        self.next_order_size = self.cfg.deal_deposit

        self.current_position_side = None
        self.position_id = None
        self.mart_current_steps = 0
        self.total_position_size = 0 #in contracts
        self.total_position_value = 0
        self.commission = 0
        self.avg_price = 0
        self.last_order_price = 0

        self.tp_price = 0
        self.sl_price = None
        self.last_update_ts = 0
        self.ts_deal_start = 0

#        self.max_leverage = self.manager.get_symbol_max_leverage(self.symbol)
#        if self.max_leverage < self.cfg.leverage:
#            log_msg(f"Max allowed leverage is less then configured: {self.max_leverage} < {self.cfg.leverage}")
#            log_msg("Setting max allowed insted of configured")
#            bingx_api.set_leverage(self.max_leverage, self.symbol)
#        else:
        try:
            bingx_api.set_leverage(self.cfg.leverage, self.symbol)
        except Exception as e:
            handle_exception(e)


    def start_strategy(self):
        klines = bingx_api.load_klines(self.symbol, self.cfg.timeframe)
        prices_arr = []
        for kline in klines:
            prices_arr.append(float(kline['close']))
        self.slow_ema = calculate_ema(prices_arr, self.cfg.ema_slow)
        self.fast_ema = calculate_ema(prices_arr, self.cfg.ema_fast)
        self.stopped = False
        self.is_updated = True

        self.config_id = db_insert_config(json.dumps(self.cfg.construct_cfg_dump()))
        self.strat_status_updated.emit(self.symbol, "STARTED")

    def rapid_stop(self):
        self.stopped = True
        self.is_updated = False

        if self.total_position_value != 0:
            order_result = bingx_api.new_market_order(self.symbol, side="SELL" if self.current_position_side == 1 else "BUY",
                                                      quantity=self.total_position_size)
            self.process_position_closed(order_result)

        self.strat_status_updated.emit(self.symbol, "STOPPED")

    def stop_updates(self):
        self.is_updated = False
        self.strat_status_updated.emit(self.symbol, "DROPPED_UPDATES")

        if self.total_position_value == 0:
            self.stopped = True
            self.strat_status_updated.emit(self.symbol, "STOPPED")

    def process_position_closed(self, order_result):
        order_id = order_result["data"]["order"]["orderId"]
        order_data = bingx_api.get_order_details(self.symbol, order_id)
        db_new_finished_order(order_data, self.position_id)

        self.commission += float(order_data["data"]["order"]["commission"]) #was negative
        position_value = float(order_data["data"]["order"]["executedQty"]) * float(order_data["data"]["order"]["avgPrice"])
        total_result = position_value - self.total_position_value if self.current_position_side == 1 else self.total_position_value - position_value

        log_msg(f"Finished deal for {self.symbol}:\n\tSide: {'LONG' if self.current_position_side == 1 else 'SHORT'}\n\t" +
              f"Avg_price open: {self.avg_price}\n\tAvg_price close: {order_data['data']['order']['avgPrice']}\n\t" +
              f"Commission: {abs(self.commission)}\n\tFinal result: {total_result}")

        deal_report = DealReport(symbol=self.symbol, timeframe=self.cfg.timeframe,
                                 direction="LONG" if self.current_position_side == 1 else "SHORT",
                                 leverage=self.cfg.leverage, ts_start=self.ts_deal_start,
                                 ts_end=time.time(), position_size=self.total_position_value,
                                 mart_steps=self.mart_current_steps,
                                 total_result=total_result, commission=abs(self.commission))

        self.manager.finished_deals.append(deal_report)
        db_new_finished_deal(self.position_id, deal_report)
        self.avg_price = 0
        self.last_order_price = 0
        self.commission = 0
        self.total_position_size = 0
        self.total_position_value = 0
        self.current_position_side = None
        self.ts_deal_start = 0
        self.position_id = None

        self.next_order_size = self.cfg.deal_deposit
        self.mart_current_steps = 0

        self.bars_delay = self.cfg.pause_bars
        self.manager.current_open_positions -= 1
        log_msg(f"{self.symbol}: current_open_positions: {self.manager.current_open_positions}")
        self.manager.update_available_funds()

        if not self.is_updated:
            self.stopped = True
            self.strat_status_updated.emit(self.symbol, "STOPPED")


    def process_new_price(self, new_price):
        if self.current_position_side == 1: #long
            if self.sl_price is not None and self.sl_price >= new_price:
                order_result = bingx_api.new_market_order(self.symbol, side="SELL", quantity=self.total_position_size)
                self.process_position_closed(order_result)
            if self.tp_price <= new_price:
                order_result = bingx_api.new_market_order(self.symbol, side="SELL", quantity=self.total_position_size)
                self.process_position_closed(order_result)
        elif self.current_position_side == -1: #short
            if self.sl_price is not None and self.sl_price <= new_price:
                order_result = bingx_api.new_market_order(self.symbol, side="BUY", quantity=self.total_position_size)
                self.process_position_closed(order_result)

            if self.tp_price >= new_price:
                order_result = bingx_api.new_market_order(self.symbol, side="BUY", quantity=self.total_position_size)
                self.process_position_closed(order_result)


        order_base = round(self.next_order_size / new_price, self.manager.get_quantity_precision(self.symbol))
        if int(time.time() / self.cfg.timeframe_duration) - self.last_update_ts == 0:
            self.last_update_ts = int(time.time() / self.cfg.timeframe_duration)
            return

        self.last_update_ts = int(time.time() / self.cfg.timeframe_duration)

        extend_ema(self.fast_ema, new_price, self.cfg.ema_fast)
        extend_ema(self.slow_ema, new_price, self.cfg.ema_slow)

        if self.current_position_side is not None and self.bars_delay > 0:
            self.bars_delay -= 1
            log_msg(f"{self.symbol}: Bars dealy left: {self.bars_delay}")

        signal = self.check_signal()
        if signal is None:
            return
        
        if self.cfg.ema_cross_tp is not None and self.current_position_side is not None and self.current_position_side != signal:
            should_close = False
            position_gain = 0
            if self.current_position_side == LONG and ((new_price - self.avg_price) / self.avg_price) > self.cfg.ema_cross_tp / 100:
                should_close = True
                position_gain = ((self.avg_price - new_price) / self.avg_price)

            if self.current_position_side == SHORT and ((self.avg_price - new_price) / self.avg_price) > self.cfg.ema_cross_tp / 100:
                should_close = True
                position_gain = ((new_price - self.avg_price) / self.avg_price)

            if should_close:
                log_msg(f"{self.symbol}: Closing position: EMA CROSS + position gain {round(position_gain*100, 2)} > min allowed: {self.cfg.ema_cross_tp}")
                order_result = bingx_api.new_market_order(self.symbol, side="SELL" if self.current_position_side == 1 else "BUY",
                                                          quantity=self.total_position_size)
                self.process_position_closed(order_result)
                return

        if not self.validate_signal(signal, new_price):
            return   

        available_funds = float(self.manager.get_available_margin())

        order_base = round(self.next_order_size / new_price, self.manager.get_quantity_precision(self.symbol))
        order_quote = order_base * new_price

        if available_funds < order_quote:
            log_msg(f"{self.symbol}: Skip signal - insufficient funds: need {order_quote}, but only {available_funds} is available")
            return

        if self.current_position_side is None:
            log_msg(f"{self.symbol}: current_open_positions: {self.manager.current_open_positions}")
            if self.manager.current_open_positions >= self.manager.max_open_positions_allowed:
                log_msg(f"{self.symbol}: Skip signal - max open position allowed exceeded")
                return

            self.current_position_side = signal
            self.ts_deal_start = time.time()
            self.manager.current_open_positions += 1
            self.position_id = db_new_deal(self)

        order_result = bingx_api.new_market_order(self.symbol, side="BUY" if signal > 0 else "SELL", quantity=order_base)
        if order_result is None: #some failure
            return

        order_id = order_result["data"]["order"]["orderId"]
        order_data = bingx_api.get_order_details(self.symbol, order_id)
        db_new_finished_order(order_data, self.position_id)

        self.commission += float(order_data["data"]["order"]["commission"]) #was negative
        self.last_order_price = float(order_data["data"]["order"]["avgPrice"])
        position_value = float(order_data["data"]["order"]["executedQty"]) * self.last_order_price
        self.total_position_size += abs(float(order_data["data"]["order"]["executedQty"]))
        self.total_position_value += position_value

        self.avg_price = self.total_position_value / self.total_position_size

        self.tp_price = self.avg_price * (100+self.current_position_side*self.cfg.tp) / 100
        if self.cfg.sl is not None:
            self.sl_price = self.avg_price * (100+self.current_position_side*self.cfg.sl*(-1)) / 100
        else:
            self.sl_price = None
        self.next_order_size *= (1+(self.cfg.mart_coef / 100))
        self.mart_current_steps += 1

        log_msg(f"{self.symbol}: Avg price: {self.avg_price}")
        log_msg(f"{self.symbol}: Last order price: {self.last_order_price}")
        log_msg(f"{self.symbol}: New Sl price: {self.sl_price}")
        log_msg(f"{self.symbol}: New Tp price: {self.tp_price}")
        log_msg(f"{self.symbol}: Mart steps: {self.mart_current_steps}")

        self.manager.update_available_funds()

    def validate_signal(self, signal, new_price):
        if self.current_position_side is None and self.cfg.allowed_direction != 0:
            if self.cfg.allowed_direction != signal:
                log_msg(f"{self.symbol}: Skip signal due to only {'LONG' if signal == 1 else 'SHORT'} signals allowed")
                return False

        if self.current_position_side is not None:
            if signal != self.current_position_side:
                log_msg(f"{self.symbol}: Opposite direction signal while aready in {'LONG' if self.current_position_side == 1 else 'SHORT'} position")
                return False

            if self.bars_delay > 0:
                log_msg(f"{self.symbol}: Skip signal due to awaited delay {self.bars_delay} more bars to wait")
                return False

            if self.mart_current_steps == self.cfg.max_mart_depth+1:
                log_msg(f"Skip signal due to max mart step reached: {self.cfg.max_mart_depth}")
                return False

            if (self.current_position_side == LONG and new_price < self.avg_price) or \
                self.current_position_side == SHORT and new_price > self.avg_price:
                price_perc_delta = abs(self.last_order_price - new_price) / self.last_order_price * 100
                if price_perc_delta < self.cfg.min_delta_perc:
                    log_msg(f"{self.symbol}: Skip signal due to perc delta less then min allowed: {price_perc_delta} < {self.cfg.min_delta_perc}")
                    return False
            else:
                log_msg(f"{self.symbol}: Skip signal due to new price goes wrong direction")
                return False
        
        return True

    def check_signal(self):
        signal = None

        if self.fast_ema[-2] < self.slow_ema[-2] and self.fast_ema[-1] > self.slow_ema[-1]:
            signal = LONG
        elif self.fast_ema[-2] > self.slow_ema[-2] and self.fast_ema[-1] < self.slow_ema[-1]:
            signal = SHORT

        return signal
