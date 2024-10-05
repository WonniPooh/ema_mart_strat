# This Python file uses the following encoding: utf-8
import json
from db_connector import db_update_balance, construct_db
from SymbolStrategy import *
from threading import Thread
import bingx_api
import queue
import websocket_server
from common import KLINES_INTERVAL_DURATION, handle_exception

MAX_CONFIGURED_STRATEGIES = 20
MAX_STRAT_IN_POSITION = 10

class StrategyCfg:
    def __init__(self):
        self.symbol = None
        self.leverage = 0
        self.timeframe = ""
        self.timeframe_index = 0
        self.timeframe_duration = 0
        self.allowed_direction = 0
        self.deal_deposit = None
        self.margin_type = None
        self.margin_type_index = None
        self.leverage = 1
        self.tp = None
        self.sl = None
        self.ema_cross_tp = None

        self.filter_enabled = False
        self.filter_tf = None
        self.filter_tf_index = 0
        self.filter_tf_duration = 0
        self.filter_ema_slow = None
        self.filter_ema_fast = None
        self.filter_max_allowed_perc_delta = None

        self.ema_slow = None
        self.ema_fast = None

        self.max_mart_depth = None
        self.mart_coef = None

        self.pause_bars = None
        self.min_delta_perc = None

        

    def parse_jsoned_cfg(self, symbol, symbol_data):
        self.symbol = symbol
        self.allowed_direction = symbol_data["allowed_direction"]
        self.deal_deposit = symbol_data["deal_deposit"]
        self.margin_type = symbol_data["margin_type"]
        self.margin_type_index = symbol_data["margin_type_index"]
        self.leverage = symbol_data["leverage"]
        self.sl = symbol_data["sl"]
        self.tp = symbol_data["tp"]
        self.timeframe = symbol_data["tf"]
        self.timeframe_index = symbol_data["tf_index"]
        self.timeframe_duration = KLINES_INTERVAL_DURATION[self.timeframe]

        self.filter_enabled = symbol_data.get("f_enabled", False)
        self.filter_tf = symbol_data.get("f_tf", "1m")
        self.filter_tf_index = symbol_data.get("f_tf_index", 0)
        self.filter_tf_duration = KLINES_INTERVAL_DURATION[self.filter_tf]
        self.filter_ema_slow = symbol_data.get("f_ema_slow")
        self.filter_ema_fast = symbol_data.get("f_ema_fast")
        self.filter_max_allowed_perc_delta = symbol_data.get("f_max_allowed_delta")

        self.ema_slow = symbol_data["ema_slow"]
        self.ema_fast = symbol_data["ema_fast"]

        self.max_mart_depth = symbol_data["max_mart_depth"]
        self.mart_coef = symbol_data["mart_coef"]

        self.pause_bars = symbol_data["pause_bars"]
        self.min_delta_perc = symbol_data["min_delta_perc"]
        self.ema_cross_tp = symbol_data.get("ema_cross_tp")

    def construct_cfg_dump(self):
        cfg_dump = {"leverage":self.leverage,
                    "allowed_direction":self.allowed_direction,
                    "deal_deposit":self.deal_deposit,
                    "tf":self.timeframe,
                    "tf_index":self.timeframe_index,
                    "margin_type":self.margin_type,
                    "margin_type_index":self.margin_type_index,
                    "tp":self.tp,
                    "sl":self.sl,
                    "ema_cross_tp":self.ema_cross_tp,
                    "ema_slow":self.ema_slow,
                    "ema_fast":self.ema_fast,
                    "max_mart_depth": self.max_mart_depth,
                    "mart_coef": self.mart_coef,
                    "pause_bars": self.pause_bars,
                    "min_delta_perc": self.min_delta_perc,

                    "f_enabled":self.filter_enabled,
                    "f_tf":self.filter_tf,
                    "f_tf_index":self.filter_tf_index,
                    "f_ema_slow":self.filter_ema_slow,
                    "f_ema_fast":self.filter_ema_fast,
                    "f_max_allowed_delta":self.filter_max_allowed_perc_delta
                    }

        return cfg_dump

class StrategyManager:
    def __init__(self):
        self.strategies = {}
        self.cmd_input_queue = queue.Queue(maxsize=10)
        self.output_queue = queue.Queue(maxsize=10)
        self.ws_server = websocket_server.run_single_thread_server(self.cmd_input_queue, self.output_queue)

        self.log_file = open("strat.log", "a")
        bingx_api.log_msg = self.show_log
        self.depo_start_val = None
        self.depo_current_val = None
        self.funds = None
        self.uid = 0

        self.balance_update_count = 10
        self.upd_balance_interval = 30_000 #ms

        self.symbols_prices = {}
        self.symbols_data = bingx_api.get_available_futures_contracts()
        self.update_available_funds()
        self.get_account_uid()

        self.max_open_positions_allowed = MAX_STRAT_IN_POSITION
        self.btc_stop_long = None
        self.btc_stop_short = None
        self.current_open_positions = 0
        self.finished_deals = []
        self.last_price_update_ts = 0 #unused atm, in future

        construct_db()

        #actually runs strategies as well
        self.upd_prices_thread = Thread(target=self.update_prices, daemon=True)
        self.upd_prices_thread.start()

        self.upd_balance_thread = Thread(target=self.update_balance, daemon=True)
        self.upd_balance_thread.start()

        is_hedge = bingx_api.is_dual_side_hedge()
        if is_hedge is not None:    
            bingx_api.ACCOUNT_STATE = int(is_hedge)


    def get_account_uid(self):
        try:
            self.uid = bingx_api.get_account_uid()["data"]["uid"]
        except Exception as e:
            self.uid = 0

    def show_log(self, log_msg):
        try:
            now = datetime.now()
            date_time = now.strftime("%d/%m, %H:%M:%S")
            final_text = date_time + " " + log_msg + "\n"
            self.post_data({"type":"info", "msg": final_text})
            print(log_msg)
            self.log_file.write(final_text)
            self.log_file.flush()
        except Exception as e:
            handle_exception(e)
            try:
                self.log_file.close()
                self.log_file = open("strat.log", "a")
            except Exception as e:
                handle_exception(e)

    def show_err(self, err_msg):
        print(err_msg)
        self.post_data({"type":"error", "msg": err_msg})

    def strat_status_updated(self, symbol, new_status):
        self.post_data({"type":"status_update", 
                        "symbol": symbol,
                        "status": new_status})
        
        if new_status == "STOPPED":
            del self.strategies[symbol]

    def start(self):
        while True:
            try:
                cmd = self.cmd_input_queue.get_nowait()
            except Exception:
                time.sleep(0.5)
                continue
            try:
                cmd = json.loads(cmd)
                
                # if cmd.get("type") == "shut_down":
                #     self.rapid_stop_all()
                #     break

                self.process_new_cmd(cmd)
            except Exception as e:
                print("Failed to process new cmd:", cmd , e)
        
    def process_new_cmd(self, command):
        if command["type"] == "uid":
            if self.uid == 0:
                self.get_account_uid()
            self.post_data({"type": "uid", "data": self.uid})
            
        if command["type"] == "account_mode":
            self.post_data({"type": "account_mode", "data": bingx_api.ACCOUNT_STATE})
        
        if command["type"] == "get_price":
            self.post_data({"type": "price", "symbol": command["symbol"], 
                            "data": self.get_symbol_price(command["symbol"])})
            
        if command["type"] == "active_deals":
            self.forward_active_deals()
            
        if command["type"] == "finished_deals":
            self.forward_finished_deals()

        if command["type"] == "running_strategies":
            self.forward_active_startegies()

        if command["type"] == "strat_config":
            self.set_strat_config(command["data"])
            self.forward_start_config()
        
        if command["type"] == "start": #config is sent in here, and deleted upon end
            self.start_strategy(command["symbol"], command["config"])

        if command["type"] == "stop":
            self.stop_single_strat(command["symbol"])

        if command["type"] == "rapid_stop":
            self.rapid_stop_single_strat(command["symbol"])


    def set_strat_config(self, config):
        try:
            max_simul_deals = config.get("max_deals")
            if max_simul_deals is not None and max_simul_deals != "":
                val = int(max_simul_deals)
                if val > MAX_STRAT_IN_POSITION:
                    self.max_open_positions_allowed = MAX_STRAT_IN_POSITION
                elif val < 1:
                    self.max_open_positions_allowed = 1
                else:
                    self.max_open_positions_allowed = val
        except:
            self.show_err("Не получилось установить ограничение на макс. кол-во одновременных сделок")
            return
        
        try:
            btc_long_stop_price = config.get("btc_long_stop")
            if btc_long_stop_price:
                if btc_long_stop_price != "":
                    self.btc_stop_long = int(btc_long_stop_price)
                else:
                    self.btc_stop_long = None
        except Exception as e:
            self.show_err(f"Не получилось считать стоп BTC ЛОНГ: {e}")
            return
        
        try:
            btc_short_stop_price = config.get("btc_short_stop")
            if btc_short_stop_price:
                if btc_short_stop_price != "":
                    self.btc_stop_short = int(btc_short_stop_price)
                else:
                    self.btc_stop_short = None
        except Exception as e:
            self.show_err(f"Не получилось считать стоп BTC ШОРТ: {e}")
            return
        
        try:
            is_hedge = int(config.get("is_hedge"))
            self.apply_account_mode(is_hedge)
        except:
            self.show_err("Не получилось установить ограничение на макс. кол-во одновременных сделок")
            return
        
    def forward_start_config(self):
        try:
            self.post_data({"type": "strat_config", 
                            "data": {"max_deals": self.max_open_positions_allowed,
                                     "btc_long_stop": self.btc_stop_long if self.btc_stop_long is not None else "",
                                     "btc_short_stop": self.btc_stop_short if self.btc_stop_short is not None else "",
                                     "is_hedge": bingx_api.ACCOUNT_STATE}})
        except Exception as e:
            handle_exception(e)

    def post_data(self, jsoned_data):
        try:
            self.output_queue.put_nowait(json.dumps(jsoned_data))
        except Exception as e:
            print("Failed to post data: ", jsoned_data, e)

    def forward_active_deals(self):
        data = []
        symbols = list(self.strategies.keys())
        symbols.sort()

        for symbol in symbols:
            if self.strategies[symbol].current_position_side is not None:
                strat = self.strategies[symbol]
                description = []
                time_deal_start = datetime.fromtimestamp(strat.ts_deal_start).strftime("%H:%M:%S")
                description.append(strat.symbol)
                description.append("LONG" if strat.current_position_side == 1 else "SHORT")
                description.append(strat.cfg.leverage)
                description.append(strat.cfg.timeframe)
                description.append(strat.total_position_value)
                description.append(round(strat.avg_price, 10))
                description.append(strat.mart_current_steps-1)
                description.append(time_deal_start)
                data.append(description)
        self.post_data({"type":"active_deals", "data": data})
    
    def forward_finished_deals(self):
        data = []
        for deal in self.finished_deals:
            data.append(deal.data_as_arr)
        self.post_data({"type":"finished_deals", "data": data})

    def forward_active_startegies(self):
        try:
            report = {}
            for symbol, start in self.strategies.items():
                strat_json_cfg = start.cfg.construct_cfg_dump() 
                strat_json_cfg["status"] = start.status
                report[symbol] = strat_json_cfg
            
            self.post_data({"type":"running_strategies", "data": report})
        except Exception as e:
            handle_exception(e)

    def apply_account_mode(self, is_hedge):
        strat_running = False
        for _, strat in self.strategies.items():
            if not strat.stopped:
                strat_running = True
                break

        if not strat_running:
            if bingx_api.ACCOUNT_STATE is not None and bingx_api.ACCOUNT_STATE == is_hedge:
                return True, None
                             
            result = bingx_api.change_dual_side(is_hedge)
            if result is None:
                bingx_api.ACCOUNT_STATE = is_hedge
                return True, None
            else:
                return False, result
        else:
            return False, None

    def start_strategy(self, symbol, config, should_run=True):
        try:
            parsed_config = StrategyCfg()
            parsed_config.parse_jsoned_cfg(symbol, config)

            strategy = self.strategies.get(symbol)
            if strategy and not strategy.stopped:
                self.show_log(f"Strategy for {symbol} already running")
                return

            if strategy:
                del self.strategies[symbol]

            strategy = SymbolStrategy(parsed_config, self, self.show_log)
            self.strategies[symbol] = strategy

            if should_run:
                self.show_log(f"Starting for {symbol}")
                strategy.start_strategy()
        except Exception as e:
            handle_exception(e)
            self.show_err(f"Не получилось запусить стратегию для {symbol}: {e}")

    def rapid_stop_single_strat(self, symbol):
        strat = self.strategies.get(symbol)
        if strat is None:
            self.show_log(f"Can't find active strat for {symbol}")
            return
        strat.rapid_stop()

    def stop_single_strat(self, symbol):
        strat = self.strategies[symbol]
        if strat is None:
            self.show_log(f"Can't find active strat for {symbol}")
            return
        if not strat.is_updated:
            self.show_log(f"{symbol}: Strategy already no updates")
            return

        strat.stop_updates()

    def rapid_stop_all(self):
        for _, strat in self.strategies.items():
            strat.rapid_stop()

    def stop_all(self):
        for _, strat in self.strategies.items():
            strat.stop_updates()

    def update_available_funds(self):
        try:
            result = bingx_api.get_balance()
            if result is not None:
                self.funds = result
        except Exception as e:
            handle_exception(e)

    def get_available_margin(self):
        try:
            return self.funds["availableMargin"]
        except Exception as e:
            handle_exception(e)
            return None

    def get_quantity_precision(self, symbol):
        return self.symbols_data[symbol]["quantityPrecision"]

    def get_symbol_max_leverage(self, symbol):
        return self.symbols_data[symbol]["maxLongLeverage"]

    def get_symbol_price(self, symbol):
        if self.symbols_prices is not None:
            return self.symbols_prices.get(symbol.upper())
        else:
            return None

    def update_prices(self):
        counter = 0
        while True:
            try:
                self.symbols_prices = bingx_api.get_current_price()
                if self.symbols_prices is None:
                    self.symbols_prices = {}

                self.last_price_update_ts = time.time()

                if self.btc_stop_long is not None or self.btc_stop_short is not None:
                    btc_price = self.symbols_prices.get("BTC-USDT")
                    if btc_price is not None:
                        if self.btc_stop_short is not None and btc_price > self.btc_stop_short:
                            for symbol, strategy in self.strategies.items():
                                if not strategy.stopped and strategy.cfg.allowed_direction <= 0:
                                    self.show_log(f"СТОП ШОРТ по цене BTC для {symbol}: текущая цена - {btc_price} > {self.btc_stop_short}")
                                    strategy.rapid_stop()

                        if self.btc_stop_long is not None and btc_price < self.btc_stop_long:
                            for symbol, strategy in self.strategies.items():
                                if not strategy.stopped and strategy.cfg.allowed_direction >= 0:
                                    self.show_log(f"СТОП ЛОНГ по цене BTC для {symbol}: текущая цена - {btc_price} < {self.btc_stop_long}")
                                    strategy.rapid_stop()
                    else:
                        self.show_log("Can't check BTC stop: No price for BTC-USDT")

                for symbol, strategy in self.strategies.items():
                    if not strategy.stopped:
                        price = self.symbols_prices.get(symbol)
                        if price is not None:
                            try:
                                strategy.process_new_price(float(price))
                            except Exception as e:
                                handle_exception(e)
                        else:
                            self.show_log(f"No price for {symbol}")

                counter += 1
                if counter >= 3:
                    self.update_available_funds()
                    counter = 0

                time.sleep(10 - time.time()%10 + 0.05)
            except Exception as e:
                handle_exception(e)

    def update_balance(self):
        while True:
            try:
                balance_info = bingx_api.get_balance()
                if balance_info is not None:
                    balance = float(balance_info["equity"])

                    if self.depo_start_val is None:
                        self.depo_start_val = balance
                    self.depo_current_val = balance
                    self.balance_update_count += 1

                    if self.balance_update_count >= 4:
                        self.balance_update_count = 0
                        db_update_balance(balance)

                    self.post_data({"type":"balance", "init": self.depo_current_val, 
                                    "current": self.depo_current_val})
                
                if len(self.finished_deals) > 200:
                    drop_size = len(self.finished_deals) - 150
                    for _ in range(drop_size):
                        del self.finished_deals[0]

                time.sleep(15 - time.time()%15 + 0.05)
                
            except Exception as e:
                handle_exception(e)
