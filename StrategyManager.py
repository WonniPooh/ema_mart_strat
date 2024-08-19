# This Python file uses the following encoding: utf-8
import json
from db_connector import db_update_balance, construct_db
from PySide6.QtCore import QObject, QThread, QTimer
from SymbolStrategy import *
from threading import Thread
import bingx_api
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
        self.direction = 0
        self.deal_deposit = None
        self.margin_type = None
        self.margin_type_index = None
        self.leverage = 1
        self.tp = None
        self.sl = None

        self.ema_slow = None
        self.ema_fast = None

        self.max_mart_depth = None
        self.mart_coef = None

        self.pause_bars = None
        self.min_delta_perc = None

    def parse_jsoned_cfg(self, symbol, symbol_data):
        self.symbol = symbol
        self.direction = symbol_data["direction"]
        self.deal_deposit = symbol_data["deal_deposit"]
        self.margin_type = symbol_data["margin_type"]
        self.margin_type_index = symbol_data["margin_type_index"]
        self.leverage = symbol_data["leverage"]
        self.sl = symbol_data["sl"]
        self.tp = symbol_data["tp"]
        self.timeframe = symbol_data["tf"]
        self.timeframe_index = symbol_data["tf_index"]
        self.timeframe_duration = KLINES_INTERVAL_DURATION[self.timeframe]

        self.ema_slow = symbol_data["ema_slow"]
        self.ema_fast = symbol_data["ema_fast"]

        self.max_mart_depth = symbol_data["max_mart_depth"]
        self.mart_coef = symbol_data["mart_coef"]

        self.pause_bars = symbol_data["pause_bars"]
        self.min_delta_perc = symbol_data["min_delta_perc"]

    def construct_cfg_dump(self):
        cfg_dump = {"leverage":self.leverage,
                    "direction":self.direction,
                    "deal_deposit":self.deal_deposit,
                    "tf":self.timeframe,
                    "tf_index":self.timeframe_index,
                    "margin_type":self.margin_type,
                    "margin_type_index":self.margin_type_index,
                    "tp":self.tp,
                    "sl":self.sl,
                    "ema_slow":self.ema_slow,
                    "ema_fast":self.ema_fast,
                    "max_mart_depth": self.max_mart_depth,
                    "mart_coef": self.mart_coef,
                    "pause_bars": self.pause_bars,
                    "min_delta_perc": self.min_delta_perc
                    }

        return cfg_dump


#if we need to cancel, we fire CANCEL + set timer that will cancel signal if no respoce in 5 seconds, and print FAILED NEW SIGNAL msg
#if order is cancelled succesfully, we cancel that timer on getting a report, and then just creating new order
#also we need to setup a separate WS for ordebook, and we need to check and at least log somewhere what is the status - like
#how far our BUY\SELL changed the market price.
#also we need to add saving results - should be easy, on parsing new order we just dump it in a file

class StrategyManager(QObject):
    def __init__(self, logger, show_balance):
        super().__init__()
        self.symbols_cfg = {}
        self.strategies = {}
        self.logger = logger
        self.show_balance = show_balance

        self.depo_start_val = None
        self.depo_current_val = None
        self.funds = None

        self.balance_update_count = 10
        self.upd_balance_interval = 30_000 #ms

        self.symbols_prices = {}
        self.symbols_data = bingx_api.get_available_futures_contracts()
        self.update_available_funds()

        self.max_open_positions_allowed = MAX_STRAT_IN_POSITION
        self.current_open_positions = 0
        self.finished_deals = []

        construct_db()

        self.upd_prices_thread = Thread(target=self.update_prices, daemon=True)
        self.upd_prices_thread.start()

        self.upd_balance_thread = Thread(target=self.update_balance, daemon=True)
        self.upd_balance_thread.start()

    def add_new_cfg(self, symbol, cfg):
        print(f"add for {symbol}")
        existed_cfg = self.symbols_cfg.get(symbol)
        if existed_cfg is not None:
            self.symbols_cfg[symbol] = cfg
            return

        if len(self.symbols_cfg) >= MAX_CONFIGURED_STRATEGIES:
            msg = f"Can't add strategy for {symbol} - max allowed strat is {MAX_CONFIGURED_STRATEGIES}; Already configured: {len(self.symbols_cfg)}"
            self.logger(msg)
            return msg
        
        self.symbols_cfg[symbol] = cfg

    def set_max_open_positions_allowed(self, val):
        if val > MAX_STRAT_IN_POSITION:
            self.max_open_positions_allowed = MAX_STRAT_IN_POSITION
        elif val < 1:
            self.max_open_positions_allowed = 1
        else:
            self.max_open_positions_allowed = val
        
        print(f"Max open positions allowed: {self.max_open_positions_allowed}")

    def update_available_funds(self):
        self.funds = bingx_api.get_balance()

    def get_available_margin(self):
        return self.funds["availableMargin"]

    def get_quantity_precision(self, symbol):
        return self.symbols_data[symbol]["quantityPrecision"]

    def get_symbol_max_leverage(self, symbol):
        print(symbol, "get_symbol_max_leverage", self.symbols_data[symbol])
        return self.symbols_data[symbol]["maxLongLeverage"]

    def start_strategies(self, update_signal_handler=None):
        for symbol in self.symbols_cfg:
            self.init_strategy(symbol, False, update_signal_handler)

        for _, strat in self.strategies.items():
            if strat.stopped:
                strat.start_strategy()

    def init_strategy(self, symbol=None, should_run=True, update_signal_handler=None):

        cfg = self.symbols_cfg.get(symbol)
        strategy = self.strategies.get(symbol)

        if strategy and not strategy.stopped:
            self.logger(f"Strategy for {symbol} already running")
            return

        if strategy:
            del self.strategies[symbol]

        strategy = SymbolStrategy(cfg, self, self.logger)

        if update_signal_handler:
            strategy.strat_status_updated.connect(update_signal_handler)

        self.strategies[symbol] = strategy

        if should_run:
            self.logger(f"Starting for {symbol}")
            strategy.start_strategy()

        return True

    def rapid_stop_single_strat(self):
        symbol = self.sender().objectName().split("_")[0]
        strat = self.strategies.get(symbol)
        if strat is None:
            self.logger(f"Can't find active strat for {symbol}")
            return
        if strat.stopped:
            self.logger(f"Already stopped")
            return

        strat.rapid_stop()

    def stop_single_strat(self):
        symbol = self.sender().objectName().split("_")[0]
        strat = self.strategies.get(symbol)
        if strat is None:
            self.logger(f"Can't find active strat for {symbol}")
            return
        if strat.stopped:
            self.logger(f"Strategy already stopped")
            return

        if not strat.is_updated:
            self.logger(f"Strategy already no updates")
            return

        strat.stop_updates()

    def rapid_stop(self):
        for symbol, strat in self.strategies.items():
            strat.rapid_stop()

    def stop(self):
        for symbol, strat in self.strategies.items():
            strat.stop_updates()

    def update_prices(self):
        while True:
            self.symbols_prices = bingx_api.get_current_price()
            for symbol, strategy in self.strategies.items():
                if not strategy.stopped:
                    price = self.symbols_prices.get(symbol)
                    if price is not None:
                        try:
                            strategy.process_new_price(float(price))
                        except Exception as e:
                            handle_exception(e)
                    else:
                        print("No price for {symbol}")

            print(f"Sleeping {10 - time.time()%10 + 0.05} before next price update")
            time.sleep(10 - time.time()%10 + 0.05)

    def update_balance(self):
        while True:
            try:
                balance_info = bingx_api.get_balance()
                balance = float(balance_info["equity"])

                if self.depo_start_val is None:
                    self.depo_start_val = balance
                self.depo_current_val = balance
                self.balance_update_count += 1

                if self.balance_update_count >= 4:
                    self.balance_update_count = 0
                    db_update_balance(balance)

                self.show_balance(self.depo_start_val, self.depo_current_val, self.depo_current_val-self.depo_start_val)
                time.sleep(15 - time.time()%15 + 0.05)
            except Exception as e:
                handle_exception(e)
