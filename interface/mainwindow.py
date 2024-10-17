    # This Python file uses the following encoding: utf-8
import sys
import time
import os
import json

from datetime import datetime
from threading import Thread


from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QHeaderView
from PySide6.QtWidgets import QMessageBox, QPushButton, QHBoxLayout
from PySide6.QtWidgets import QWidget, QRadioButton, QLabel, QCheckBox

from PySide6.QtCore import Qt, QAbstractTableModel
from PySide6.QtGui import QBrush

from common import *
from WsConnector import WsConnector
from report_construction import RunningDealsDataTableModel, FinishedDealsDataTableModel, ReportManager

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.m_thread = Thread(target=self.run_time_since_start_counter, daemon=True)
        self.m_thread.start()

        self.report_manager = ReportManager(self)
        self.log_file = open("strat.log", "a")
        self.allowed_uid = "8768769"
        self.current_balance_color = ""
        self.ts_start = int(time.time())

        self.managed_symbols_layouts = {}
        self.managed_symbols_indicators = {}

        self.ui.start_all_btn.clicked.connect(self.startStrategies)
        self.ui.load_cfg_btn.clicked.connect(self.loadConfig)
        self.ui.save_cfg_btn.clicked.connect(self.saveConfig)
        self.ui.add_asset_cfg_btn.clicked.connect(self.addNewAssetCfg)
        self.ui.clean_input_btn.clicked.connect(self.cleanCfgInput)
        self.ui.refresh_open_deals_btn.clicked.connect(self.refreshOpenDeals)
        self.ui.refresh_finished_deals_btn.clicked.connect(self.refreshFinishedDeals)
        self.ui.apply_strat_settings_btn.clicked.connect(self.setStratSettings)
        self.ui.update_btc_price_btn.clicked.connect(self.request_btc_price)

        self.ui.deal_deposit_input.textChanged.connect(self.update_max_deal_deposit)
        self.ui.max_mart_depth_input.textChanged.connect(self.update_max_deal_deposit)
        self.ui.mart_coef_input.textChanged.connect(self.update_max_deal_deposit)

        self.ui.rapid_stop_all_btn.clicked.connect(self.rapidStopStrategies)
        self.ui.stop_all_btn.clicked.connect(self.stopStrategies)
        self.deals_report_brief = []
        self.acc_uid = None
        self.configured_strategies = {}

        self.ws_connection = WsConnector(self.wsMsgProcessor, self.onWsConnectionEstablished)

    def onWsConnectionEstablished(self):
        self.request_account_uid()
        self.request_account_mode()
        self.request_running_strat()

    def wsMsgProcessor(self, msg):
        try:
            parsed = json.loads(msg)
            msg_type = parsed.get("type")

            if msg_type == "error":
                self.popError(parsed["msg"])

            if msg_type == "info":
                self.show_log(parsed["msg"])

            if msg_type == "price":
                if parsed["symbol"] == "BTC-USDT":
                    self.update_btc_price_lbl(parsed["data"])
            
            if msg_type == "uid":
                self.setUid(parsed["data"])

            if msg_type == "account_mode":
                self.displayAccMode(parsed["data"])

            if msg_type == "active_deals":
                self.displayOpenDeals(parsed["data"])

            if msg_type == "finished_deals":
                self.displayFinishedDeals(parsed["data"])

            if msg_type == "running_strategies":
                self.addConfigs(parsed["data"])

            if msg_type == "strat_config":
                self.showStratSettings(parsed["data"])

            if msg_type == "balance":
                self.update_balance_lbl(float(parsed["init"]), float(parsed["current"]))

            if msg_type == "status_update":
                self.on_strat_new_status(parsed["symbol"], parsed["status"])

        except Exception as e:
            handle_exception(e)

    def displayAccMode(self, mode):
        self.ui.account_mode_input.setCurrentIndex(int(mode))

    def setUid(self, uid):
        if uid != 0:
            self.acc_uid = uid
        else:
            self.popError(f"Не получилось получить UID! Попробуйте перезагрузить программу")

    def request_running_strat(self):
        self.ws_connection.send_message(json.dumps({"type":"running_strategies"}))

    def request_account_uid(self):
        self.ws_connection.send_message(json.dumps({"type":"uid"}))

    def request_account_mode(self):
        self.ws_connection.send_message(json.dumps({"type":"account_mode"}))

    def check_uid(self):
        return True
        if self.acc_uid is None:
            self.request_account_uid()
            self.popError("Не могу получить ID аккаунта! Проверьте что стратегия запущена и попытайтесь снова!")
        else:
            if self.acc_uid != int("1" + "0"*len(self.allowed_uid)) - int(self.allowed_uid):
                self.popError("UID аккаунта не совпадает с разрешённым! Проверьте что АПИ-ключи от нужного аккаунта")
                return False
            else:
                return True

    def showStratSettings(self, settings):
        try:
            self.ui.max_simultaneous_deals_input.setText(str(settings["max_deals"]))
            self.ui.btc_stop_long_input.setText(str(settings["btc_long_stop"]))
            self.ui.btc_stop_short_input.setText(str(settings["btc_short_stop"]))
            self.ui.account_mode_input.setCurrentIndex(int(settings["is_hedge"]))
        except Exception as e:
            handle_exception(e)

    def setStratSettings(self):
        try:
            max_simul_deals = self.ui.max_simultaneous_deals_input.text()
            btc_long_stop_price = self.ui.btc_stop_long_input.text()
            btc_short_stop_price = self.ui.btc_stop_short_input.text()
            accout_mode = self.ui.account_mode_input.currentIndex()


            self.ws_connection.send_message(json.dumps({"type": "strat_config", 
                                                        "data": {"max_deals": max_simul_deals,
                                                                "btc_long_stop": btc_long_stop_price,
                                                                "btc_short_stop": btc_short_stop_price,
                                                                "is_hedge": int(accout_mode)}}))
        except Exception as e:
            handle_exception(e)   

    def refreshFinishedDeals(self):
        self.ws_connection.send_message(json.dumps({"type":"finished_deals"}))

    def displayFinishedDeals(self, finished_deals):
        if len(finished_deals) > 0:
            model = FinishedDealsDataTableModel(finished_deals)
            self.ui.finished_deals_table.setModel(model)
        else:
            self.show_log("Невозможно обновить - Данные отсутствуют")

    def refreshOpenDeals(self):
        self.ws_connection.send_message(json.dumps({"type":"active_deals"}))

    def displayOpenDeals(self, running_deals):
        model = RunningDealsDataTableModel(running_deals)
        self.ui.open_deals_table.setModel(model)
        if len(running_deals) == 0:
            self.show_log("Данные отсутствуют")

    def startStrategies(self):
        if not self.check_uid():
            return

        if len(self.configured_strategies) == 0:
            self.popError("Нечего делать - нет сконфигурированных стратегий")
        
        for symbol, config in self.configured_strategies.items():
            self.ws_connection.send_message(json.dumps({"type":"start", 
                                                        "symbol":symbol, 
                                                        "config": config["cfg"]}))      


    def stopSingleStrat(self):
        symbol = self.sender().objectName().split("_")[0]
        config = self.configured_strategies[symbol]
        if config["status"] == "STARTED":
            self.ws_connection.send_message(json.dumps({"type":"stop", 
                                                        "symbol":symbol}))
    
    def rapidStopSingleStrat(self):
        symbol = self.sender().objectName().split("_")[0]

        config = self.configured_strategies[symbol]
        if config["status"] != "STOPPED":
            self.ws_connection.send_message(json.dumps({"type":"rapid_stop", 
                                                        "symbol":symbol}))

    def stopStrategies(self):
        for symbol, config in self.configured_strategies.items():
            if config["status"] == "STARTED":
                self.ws_connection.send_message(json.dumps({"type":"stop", 
                                                            "symbol":symbol}))

    def rapidStopStrategies(self):
        for symbol, config in self.configured_strategies.items():
            if config["status"] != "STOPPED":
                self.ws_connection.send_message(json.dumps({"type":"rapid_stop", 
                                                            "symbol":symbol}))
    
    def startSingleStrat(self):
        if not self.check_uid():
            return
        symbol = self.sender().objectName().split("_")[0]
        
        self.ws_connection.send_message(json.dumps({"type":"start", 
                                                    "symbol":symbol, 
                                                    "config": self.configured_strategies[symbol]["cfg"]}))  

    def on_strat_new_status(self, symbol, status):
        indicator = self.managed_symbols_indicators[symbol]
        self.configured_strategies[symbol]["status"] = status
        if status == "STOPPED":
            self.set_indicator_color(indicator, "red")
        elif status == "STARTED":
            self.set_indicator_color(indicator, "lightgreen")
        elif status == "DROPPED_UPDATES":
            self.set_indicator_color(indicator, "yellow")



    def request_btc_price(self):
        self.ws_connection.send_message(json.dumps({"type":"get_price", "symbol":"BTC-USDT"}))
    
    def update_btc_price_lbl(self, price):
        if price is not None:
            self.ui.current_btc_price_lbl.setText(str(price))
        else:
            self.popError("Не получилось получить цену!")

    def update_balance_lbl(self, start, current):
        delta = current - start
        self.ui.depo_start_val.setText(str(round(start, 1)))
        self.ui.depo_current_val.setText(str(round(current,1)))
        if delta < 0 and self.current_balance_color != "RED":
            self.ui.depo_delta_val.setStyleSheet("background: rgb(237, 51, 59); font: 11pt \"Cantarell\"; color: rgb(0, 0, 0);")
            self.current_balance_color = "RED"

        if delta > 0 and self.current_balance_color != "GREEN":
            self.ui.depo_delta_val.setStyleSheet("background: rgb(143, 240, 164); font: 11pt \"Cantarell\"; color:  rgb(0, 0, 0);")
            self.current_balance_color = "GREEN"

        if delta == 0 and self.current_balance_color != "":
            self.ui.depo_delta_val.setStyleSheet("")
            self.current_balance_color = ""

        self.ui.depo_delta_val.setText(str(round(delta,1)))

    def run_time_since_start_counter(self):
        def get_time_since_start_str():
            value = int(time.time()) - self.ts_start
            result = ""
            m = int(value / 60)
            h = 0
            d = 0
            if m > 60:
                h = int(m / 60)
                m -= h*60

            if h > 24:
                d = int(h/24)
                h -= d*24

            if d > 0:
                result += f"{d}д. "
            if h > 0:
                result += f"{h}ч. "
            if m > 0:
                result += f"{m}м."
            return result

        while(True):
            time.sleep(1)
            self.ui.tss_val.setText(get_time_since_start_str())
            while True:
                try:
                    msg = MSG_QUEUE.get_nowait()
                    self.show_log(msg)
                except:
                    break

    def loadConfig(self):
        is_running = False
        for _, strat in self.configured_strategies.items():
            if strat["status"] != "STOPPED":
                is_running = True
                break

        if is_running:
            self.popError(f"Невозможно загрузить конфигурацию при хоть 1й запущенной стратегии")
            return

        file_filter = "JSON files (*.json)"
        cfg_filename = QFileDialog.getOpenFileName(parent=self,
                                                   caption="Select config file to load:",
                                                   dir=os.getcwd() + "/configs",
                                                   filter=file_filter)
        loaded_cfg = None
        with open(cfg_filename[0], "r") as f:
            data = f.read()
            loaded_cfg = json.loads(data)

        managed_symbols = list(self.configured_strategies.keys())

        for symbol in managed_symbols:
            self.deleteManagedSymbol(symbol)

        self.addConfigs(loaded_cfg)

    def addConfigs(self, loaded_cfg):
        symbols = list(loaded_cfg.keys())
        symbols.sort()

        for symbol in symbols:
            symbol_data = loaded_cfg[symbol]
            status = symbol_data.get("status")
            
            if status is not None:
                del symbol_data["status"]
            else:
                status = "STOPPED"
            
            self.configured_strategies[symbol] = {"cfg": symbol_data, 
                                                  "status": status}
            self.addManageButtons(symbol)
            self.on_strat_new_status(symbol, status)
        self.updateTotalSymbols()

    def saveConfig(self):
        file_filter = "JSON files (*.json)"
        cfg_filename = QFileDialog.getSaveFileName(parent=self,
                                                   caption="Choose filename to save config to:",
                                                   dir=os.getcwd() + "/configs",
                                                   filter=file_filter)
        if cfg_filename[0] == "":
            return

        symbols_config = {}
        for symbol in self.configured_strategies:
            data = self.configured_strategies[symbol]
            symbols_config[symbol] = data["cfg"]

        str_cfg = json.dumps(symbols_config)
        with open(cfg_filename[0], "w") as f:
            f.write(str_cfg)

    def addNewAssetCfg(self):
        symbol = self.ui.symbol_input.text()
        symbol = symbol.upper()

        strat_cfg = self.configured_strategies.get(symbol)

        if strat_cfg is not None and strat_cfg["status"] != "STOPPED":
            self.popError("Невозможно добавить конфигурацию для актива при запущенной стратегии")
            return

        if len(self.configured_strategies) >= MAX_CONFIGURED_STRATEGIES:
            self.popError(f"Невозможно добавить конфигурацию - максимальное разрешённое число конфигураций {MAX_CONFIGURED_STRATEGIES}")
            return

        cfg = {}

        #TODO max_leverage check
        try:
            leverage = int(self.ui.leverage_input.text())
        except Exception as e:
            self.popError(f"Не могу считать плечо: " + str(e))
            return

        try:
            ema_slow = float(self.ui.slow_ema_period_input.text())
        except Exception as e:
            self.popError(f"Не могу считать медленную ЕМА: " + str(e))
            return

        try:
            ema_fast = float(self.ui.fast_ema_period_input.text())
        except Exception as e:
            self.popError(f"Не могу считать быструю ЕМА: " + str(e))
            return

        try:
            max_mart_depth = float(self.ui.max_mart_depth_input.text())
        except Exception as e:
            self.popError(f"Не могу считать макс глубну Мартингейла: " + str(e))
            return

        try:
            mart_coef = float(self.ui.mart_coef_input.text())
        except Exception as e:
            self.popError(f"Не могу считать коэф. Мартингейла: " + str(e))
            return

        try:
            pause_bars = float(self.ui.pause_bars_num_input.text())
        except Exception as e:
            self.popError(f"Не могу считать кол-во баров паузу: " + str(e))
            return

        try:
            min_delta_perc = float(self.ui.min_delta_perc_input.text())
        except Exception as e:
            self.popError(f"Не могу считать минимальную дельту для докупа: " + str(e))
            return

        try:
            deal_deposit = int(float(self.ui.deal_deposit_input.text()))
        except Exception as e:
            self.popError(f"Не могу считать депозит на сделку: " + str(e))
            return

        try:
            sl = self.ui.sl_input.text()
            if sl != "":
                sl_val = float(sl)
            else:
                sl_val = None
        except Exception as e:
            self.popError(f"Не могу считать значение Стопа: " + str(e))
            return

        try:
            tp_val = float(self.ui.tp_input.text())
        except Exception as e:
            self.popError(f"Не могу считать значение ТП: " + str(e))
            return
        
        try:
            ema_tp = self.ui.ema_cross_tp_input.text()
            if ema_tp != "":
                ema_cross_tp_val  = float(ema_tp)
            else:
                ema_cross_tp_val = None
        except Exception as e:
            self.popError(f"Не могу считать значение EMA_CROSS_TP: " + str(e))
            return

        filter_enbaled = self.ui.filter_enabled_chkbx.isChecked()
        filter_ema_slow = 0
        filter_ema_fast = 0
        filter_perc_allowed = 0

        try:
            filter_ema_slow = float(self.ui.filter_slow_ema_period_input.text())
        except Exception as e:
            if filter_enbaled:    
                self.popError(f"Фильтр: Не могу считать медленную ЕМА: " + str(e))
                return

        try:
            filter_ema_fast = float(self.ui.filter_fast_ema_period_input.text())
        except Exception as e:
            if filter_enbaled:
                self.popError(f"Фильтр: Не могу считать быструю ЕМА: " + str(e))
                return

        try:
            filter_perc_allowed = self.ui.filter_delta_limit.text()
            if filter_perc_allowed != "":
                filter_perc_allowed  = float(filter_perc_allowed)
            else:
                filter_perc_allowed = 0
        except Exception as e:
            if filter_enbaled:
                self.popError(f"Фильтр: Не могу считать Макс. Дельту: " + str(e))
                return

        if self.ui.filter_enabled_chkbx.isChecked():
            cfg["f_enabled"] = True
        else:
            cfg["f_enabled"] = False

        if self.ui.filter_disable_position_add_chkbx.isChecked():
            cfg["f_add_pos_disabled"] = True
        else:
            cfg["f_add_pos_disabled"] = False

        if ema_slow < ema_fast:
            self.popError(f"Быстрая ЕМА не может быть медленнее!")
            return

        if filter_ema_slow < filter_ema_fast:
            self.popError(f"Фильтр: Быстрая ЕМА не может быть медленнее!")
            return

        cfg["f_tf"] = self.ui.filter_tf_input.currentText()
        cfg["f_tf_index"] = self.ui.filter_tf_input.currentIndex()
        cfg["f_ema_slow"] = filter_ema_slow
        cfg["f_ema_fast"] = filter_ema_fast
        cfg["f_max_allowed_delta"] = filter_perc_allowed

        cfg["symbol"] = symbol
        cfg["leverage"] = leverage
        cfg["sl"] = sl_val
        cfg["tp"] = tp_val
        cfg["ema_cross_tp"] = ema_cross_tp_val
        cfg["ema_slow"] = ema_slow
        cfg["ema_fast"] = ema_fast
        cfg["pause_bars"] = pause_bars
        cfg["min_delta_perc"] = min_delta_perc
        cfg["max_mart_depth"] = max_mart_depth
        cfg["mart_coef"] = mart_coef
        cfg["tf"] = self.ui.tf_input.currentText()
        cfg["tf_index"] = self.ui.tf_input.currentIndex()

        cfg["deal_deposit"] = float(deal_deposit)
        cfg["margin_type"] = self.ui.margin_type_input.currentText()
        cfg["allowed_direction"] = self.ui.allowed_direction_input.currentIndex()
        if cfg["allowed_direction"] == 2:
            cfg["allowed_direction"] = -1
        cfg["margin_type_index"] = self.ui.margin_type_input.currentIndex()

        if strat_cfg is not None:
            ret = QMessageBox.question(self,'', "Данный символ уже добавлен.\n Добавить символ с новой конфигурацией?", QMessageBox.Yes | QMessageBox.No)

            if ret == QMessageBox.No:
                return
        
        strat_cfg = {"status": "STOPPED",
                     "cfg": cfg}

        self.configured_strategies[symbol] = strat_cfg

        self.addManageButtons(symbol)
        self.updateTotalSymbols()

    def showSymbolConfig(self):
        symbol = self.sender().objectName().split("_")[0]
        cfg = self.configured_strategies[symbol]["cfg"]

        self.ui.symbol_input.setText(symbol)
        self.ui.leverage_input.setText(str(cfg["leverage"]))
        self.ui.deal_deposit_input.setText(str(cfg["deal_deposit"]))
        self.ui.margin_type_input.setCurrentIndex(cfg["margin_type_index"])
        if cfg["allowed_direction"] != -1:
            self.ui.allowed_direction_input.setCurrentIndex(cfg["allowed_direction"])
        else:
            self.ui.allowed_direction_input.setCurrentIndex(2)
        self.ui.tp_input.setText(str(cfg["tp"]))
        if cfg["sl"] is not None:
            self.ui.sl_input.setText(str(cfg["sl"]))
        else:
            self.ui.sl_input.setText("")
        if cfg["ema_cross_tp"] is not None:
            self.ui.ema_cross_tp_input.setText(str(cfg["ema_cross_tp"]))

        self.ui.tf_input.setCurrentIndex(cfg["tf_index"])
        self.ui.slow_ema_period_input.setText(str(cfg["ema_slow"]))
        self.ui.fast_ema_period_input.setText(str(cfg["ema_fast"]))
        self.ui.max_mart_depth_input.setText(str(cfg["max_mart_depth"]))
        self.ui.mart_coef_input.setText(str(cfg["mart_coef"]))
        self.ui.pause_bars_num_input.setText(str(cfg["pause_bars"]))
        self.ui.min_delta_perc_input.setText(str(cfg["min_delta_perc"]))

        if cfg["f_enabled"]:
            self.ui.filter_enabled_chkbx.setChecked(True)
        else:
            self.ui.filter_enabled_chkbx.setChecked(False)
        
        if cfg.get("f_add_pos_disabled"):
            self.ui.filter_disable_position_add_chkbx.setChecked(True)
        else:
            self.ui.filter_disable_position_add_chkbx.setChecked(False)

        self.ui.filter_slow_ema_period_input.setText(str(cfg["f_ema_slow"]) if cfg["f_ema_slow"] else "")
        self.ui.filter_fast_ema_period_input.setText(str(cfg["f_ema_fast"]) if cfg["f_ema_fast"] else "")
        self.ui.filter_delta_limit.setText(str(cfg["f_max_allowed_delta"]) if cfg["f_max_allowed_delta"] else "")
        self.ui.filter_tf_input.setCurrentIndex(cfg["f_tf_index"])

    def deleteManagedSymbol(self, symbol=False):
        if symbol is False:
            symbol = self.sender().objectName().split("_")[0]

        strat = self.configured_strategies.get(symbol)

        if strat and strat["status"] != "STOPPED":
            self.popError(f"Стратегия запущена, удаление невозможно")
            return

        #dataManager state for removal
        self.show_log(f"Removed managed symbol {symbol}")
        widget = self.managed_symbols_layouts[symbol]
        self.ui.configuredSymbolsVLayout.removeWidget(widget)
        widget.deleteLater()
        del self.managed_symbols_indicators[symbol]
        del self.managed_symbols_layouts[symbol]
        del self.configured_strategies[symbol]
        self.updateTotalSymbols()

    def set_indicator_color(self, indicator, color):
        indicator.setStyleSheet("QRadioButton::indicator"
                                           "{"
                                           f"background-color : {color}"
                                           "}")

    def update_max_deal_deposit(self):
        try:
            first_deal_deposit = self.ui.deal_deposit_input.text()
            addition_orders_num = self.ui.max_mart_depth_input.text()
            mart_coef = self.ui.mart_coef_input.text()

            if mart_coef != "" and addition_orders_num != "" and first_deal_deposit != "":
                last_deal_deposit = float(first_deal_deposit)
                max_deal_deposit = last_deal_deposit
                mart_coef = float(mart_coef)/100 + 1
                addition_orders_num = int(float(addition_orders_num))
                
                for _ in range(1, addition_orders_num+1):
                    last_deal_deposit *= mart_coef
                    max_deal_deposit += last_deal_deposit

                max_deal_deposit = int(max_deal_deposit)
                self.ui.max_deal_deposit.setText(str(max_deal_deposit))
            else:
                self.ui.max_deal_deposit.setText("")
        except Exception as e:
            handle_exception(e)

    def addManageButtons(self, symbol):
        if symbol in self.managed_symbols_layouts:
            return

        hbox = QHBoxLayout()
        widget = QWidget(objectName=f'{symbol}_btn_widget')
        widget.setLayout(hbox)

        radio_indicator = QRadioButton()
        radio_indicator.setText("")
        radio_indicator.setCheckable(False)
        self.set_indicator_color(radio_indicator, "red")

        symbol_btn = QPushButton(f"{symbol}", objectName=f'{symbol}_cfg')
        delete_btn = QPushButton(f"Delete", objectName=f'{symbol}_delete')
        start_btn = QPushButton(f"START", objectName=f'{symbol}_start')
        rapid_stop_btn = QPushButton(f"STOP", objectName=f'{symbol}_stop')
        stop_updates_btn = QPushButton(f"NO_UPD", objectName=f'{symbol}_stop_update')

        symbol_btn.clicked.connect(self.showSymbolConfig)
        delete_btn.clicked.connect(self.deleteManagedSymbol)
        start_btn.clicked.connect(self.startSingleStrat)
        rapid_stop_btn.clicked.connect(self.rapidStopSingleStrat)
        stop_updates_btn.clicked.connect(self.stopSingleStrat)

        hbox.addWidget(radio_indicator)
        hbox.addWidget(symbol_btn)
        hbox.addWidget(delete_btn)
        hbox.addWidget(start_btn)
        hbox.addWidget(rapid_stop_btn)
        hbox.addWidget(stop_updates_btn)

        self.managed_symbols_indicators[symbol] = radio_indicator
        self.managed_symbols_layouts[symbol] = widget
        self.ui.configuredSymbolsVLayout.addWidget(widget)

    def updateTotalSymbols(self):
        self.ui.total_symbols_val.setText(str(len(self.managed_symbols_layouts.keys())))

    def popError(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(text)
        msg.setWindowTitle("Error")
        msg.exec()

    def cleanCfgInput(self):
        self.ui.symbol_input.clear()
        self.ui.leverage_input.clear()
        self.ui.margin_type_input.setCurrentIndex(0)
        self.ui.allowed_direction_input.setCurrentIndex(0)

        self.ui.sl_input.clear()
        self.ui.tp_input.clear()
        self.ui.ema_cross_tp_input.clear()
        self.ui.deal_deposit_input.clear()

        self.ui.slow_ema_period_input.clear()
        self.ui.fast_ema_period_input.clear()
        self.ui.max_mart_depth_input.clear()
        self.ui.mart_coef_input.clear()
        self.ui.pause_bars_num_input.clear()
        self.ui.min_delta_perc_input.clear()

        self.ui.filter_enabled_chkbx.setChecked(False)
        self.ui.filter_disable_position_add_chkbx.setChecked(False)
        self.ui.filter_slow_ema_period_input.clear()
        self.ui.filter_fast_ema_period_input.clear()
        self.ui.filter_delta_limit.clear()

    def closeEvent(self,event):
        result = QMessageBox.question(self,
                      "Confirm Exit...",
                      "Are you sure you want to exit ?",
                      QMessageBox.Yes| QMessageBox.No)
        event.ignore()

        if result == QMessageBox.Yes:
            self.ws_connection.send_message(json.dumps({"type":"shut_down"}))
            event.accept()

    def show_log(self, text):
        try:
            now = datetime.now()
            date_time = now.strftime("%d/%m, %H:%M:%S")
            final_text = date_time + " " + text + "\n"
            self.ui.logger_field.append(final_text)
            self.log_file.write(final_text)
            self.log_file.flush()
        except Exception as e:
            handle_exception(e)
            try:
                self.log_file.close()
                self.log_file = open("interface.log", "a")
            except Exception as e:
                handle_exception(e)

