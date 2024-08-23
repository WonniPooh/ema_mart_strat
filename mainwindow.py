    # This Python file uses the following encoding: utf-8
import sys
import time
import os
import json

from datetime import datetime
from threading import Thread


from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QHeaderView
from PySide6.QtWidgets import QMessageBox, QPushButton, QHBoxLayout
from PySide6.QtWidgets import QWidget, QRadioButton, QLabel

from PySide6.QtCore import Qt, QAbstractTableModel
from PySide6.QtGui import QBrush

from common import *
from StrategyManager import *
from report_construction import RunningDealsDataTableModel, FinishedDealsDataTableModel
from bingx_api import get_account_uid

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

        self.log_file = open("strat.log", "a")
        self.current_balance_color = ""
        self.ts_start = int(time.time())

        self.managed_symbols_layouts = {}
        self.managed_symbols_indicators = {}

        self.strat_manager = StrategyManager(self.show_log, self.update_balance_lbl)

        self.ui.start_all_btn.clicked.connect(self.startStrategies)
        self.ui.load_cfg_btn.clicked.connect(self.loadConfig)
        self.ui.save_cfg_btn.clicked.connect(self.saveConfig)
        self.ui.add_asset_cfg_btn.clicked.connect(self.addNewAssetCfg)
        self.ui.clean_input_btn.clicked.connect(self.cleanCfgInput)
        self.ui.refresh_open_deals_btn.clicked.connect(self.refreshOpenDeals)
        self.ui.refresh_finished_deals_btn.clicked.connect(self.refreshFinishedDeals)
        self.ui.max_simultaneous_deals_btn.clicked.connect(self.applyMaxSimulDeals)

        self.ui.rapid_stop_all_btn.clicked.connect(self.rapidStopStrategies)
        self.ui.stop_all_btn.clicked.connect(self.stopStrategies)
        self.deals_report_brief = []

        self.allowed_uid = 24942028

    def check_uid(self):
        account_uid = get_account_uid()
        if account_uid["data"]["uid"] != self.allowed_uid:
            self.popError("UID аккаунта не совпадает с разрешённым! Проверьте что АПИ-ключи от нужного аккаунта")
            return False
        else:
            return True

    def applyMaxSimulDeals(self):
        max_simul_deals = self.ui.max_simultaneous_deals_input.text()
        if max_simul_deals != "":
            try:
                max_simul_deals = int(max_simul_deals)
                self.strat_manager.set_max_open_positions_allowed(max_simul_deals)
            except Exception as e:
                self.popError("Не получилось считать ограничение на макс. кол-во одновременных сделок")

    def closeEvent(self,event):
        result = QMessageBox.question(self,
                      "Confirm Exit...",
                      "Are you sure you want to exit ?",
                      QMessageBox.Yes| QMessageBox.No)
        event.ignore()

        if result == QMessageBox.Yes:
            event.accept()

    def show_log(self, text):
        now = datetime.now()
        date_time = now.strftime("%d/%m, %H:%M:%S")
        final_text = date_time + " " + text + "\n"
        self.ui.logger_field.append(final_text)
        self.log_file.write(final_text)
        self.log_file.flush()

    def refreshFinishedDeals(self):
        if len(self.strat_manager.finished_deals) > 0:
            model = FinishedDealsDataTableModel(self.strat_manager.finished_deals)
            self.ui.finished_deals_table.setModel(model)
        else:
            self.show_log("Невозможно обновить - Данные отсутствуют")

    def refreshOpenDeals(self):
        data = []
        symbols = list(self.strat_manager.strategies.keys())
        symbols.sort()

        ["Инструмент", "Направление", "Плечо", "ТФ(мин)",
         "Вложено $", "Сред. Цена", "Шаг Март.", "Время Открытия"]
        for symbol in symbols:
            if self.strat_manager.strategies[symbol].current_position_side is not None:
                strat = self.strat_manager.strategies[symbol]
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

        model = RunningDealsDataTableModel(data)
        self.ui.open_deals_table.setModel(model)
        if len(data) == 0:
            self.show_log("Данные отсутствуют")

    def startStrategies(self):
        if not self.check_uid():
            return

        is_all_running = True
        if len(self.strat_manager.strategies) == 0:
            is_all_running = False
        else:
            for strat in self.strat_manager.strategies.values():
                if strat.stopped:
                    is_all_running = False
                    break
        if not is_all_running:
            self.strat_manager.start_strategies(self.on_strat_new_status)
        else:
            self.popError("Нечего делать - ВСЁ стратегии запущены")


    def stopStrategies(self):
        self.strat_manager.stop()

    def rapidStopStrategies(self):
        is_running = False
        for strat in self.strat_manager.strategies.values():
            if not strat.stopped:
                is_running = True
                break

        if is_running:
            self.strat_manager.rapid_stop()
        else:
            self.popError("Нечего делать - Ни одна стратегия НЕ запущена")
            return

    def on_strat_new_status(self, symbol, status):
        indicator = self.managed_symbols_indicators[symbol]
        if status == "STOPPED":
            self.set_indicator_color(indicator, "red")
        elif status == "STARTED":
            self.set_indicator_color(indicator, "lightgreen")
        elif status == "DROPPED_UPDATES":
            self.set_indicator_color(indicator, "yellow")

    def update_balance_lbl(self, start, current, delta):
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
        for _, strat in self.strat_manager.strategies.items():
            if not strat.stopped:
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

        managed_symbols = list(self.strat_manager.symbols_cfg.keys())

        for symbol in managed_symbols:
            self.deleteManagedSymbol(symbol)

        symbols = list(loaded_cfg.keys())
        symbols.sort()

        for symbol in symbols:
            symbol_data = loaded_cfg[symbol]
            cfg = StrategyCfg()
            cfg.parse_jsoned_cfg(symbol, symbol_data)
            result = self.strat_manager.add_new_cfg(symbol, cfg)
            if result:
                self.popError(result)
                continue
            self.addManageButtons(symbol)
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
        for symbol in self.strat_manager.symbols_cfg:
            data = self.strat_manager.symbols_cfg[symbol]
            symbols_config[symbol] = data.construct_cfg_dump()

        str_cfg = json.dumps(symbols_config)
        with open(cfg_filename[0], "w") as f:
            f.write(str_cfg)

    def addNewAssetCfg(self):
        symbol = self.ui.symbol_input.text()
        symbol = symbol.upper()

        strat = self.strat_manager.strategies.get(symbol)

        if strat is not None and strat.stopped == False:
            self.popError("Невозможно добавить конфигурацию для актива при запущенной стратегии")
            return

        cfg = StrategyCfg()

#        if symbol not in self.strat_manager.symbols_data:
#            self.popError(f"Invalid Symbol: {symbol}")
#            return

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

        cfg.symbol = symbol
        cfg.leverage = leverage
        cfg.sl = sl_val
        cfg.tp = tp_val
        cfg.ema_cross_tp = ema_cross_tp_val
        cfg.ema_slow = ema_slow
        cfg.ema_fast = ema_fast
        cfg.pause_bars = pause_bars
        cfg.min_delta_perc = min_delta_perc
        cfg.max_mart_depth = max_mart_depth
        cfg.mart_coef = mart_coef
        cfg.timeframe = self.ui.tf_input.currentText()
        cfg.timeframe_index = self.ui.tf_input.currentIndex()
        cfg.timeframe_duration = KLINES_INTERVAL_DURATION[cfg.timeframe]

        cfg.deal_deposit = float(deal_deposit)
        cfg.margin_type = self.ui.margin_type_input.currentText()
        cfg.allowed_direction = self.ui.allowed_direction_input.currentIndex()
        if cfg.allowed_direction == 2:
            cfg.allowed_direction = -1
        cfg.margin_type_index = self.ui.margin_type_input.currentIndex()

        if symbol in self.strat_manager.symbols_cfg:
            ret = QMessageBox.question(self,'', "Данный символ уже добавлен.\n Добавить символ с новой конфигурацией?", QMessageBox.Yes | QMessageBox.No)

            if ret == QMessageBox.No:
                return

        result = self.strat_manager.add_new_cfg(symbol, cfg)
        if result is not None:
            self.popError(result)
            return

        self.addManageButtons(symbol)
        self.updateTotalSymbols()

    def showSymbolConfig(self):
        symbol = self.sender().objectName().split("_")[0]
        cfg = self.strat_manager.symbols_cfg[symbol]

        self.ui.symbol_input.setText(symbol)
        self.ui.leverage_input.setText(str(cfg.leverage))
        self.ui.deal_deposit_input.setText(str(cfg.deal_deposit))
        self.ui.margin_type_input.setCurrentIndex(cfg.margin_type_index)
        if cfg.allowed_direction != -1:
            self.ui.allowed_direction_input.setCurrentIndex(cfg.allowed_direction)
        else:
            self.ui.allowed_direction_input.setCurrentIndex(2)
        self.ui.tp_input.setText(str(cfg.tp))
        if cfg.sl is not None:
            self.ui.sl_input.setText(str(cfg.sl))
        else:
            self.ui.sl_input.setText("")
        if cfg.ema_cross_tp is not None:
            self.ui.ema_cross_tp_input.setText(str(cfg.ema_cross_tp))

        self.ui.slow_ema_period_input.setText(str(cfg.ema_slow))
        self.ui.fast_ema_period_input.setText(str(cfg.ema_fast))
        self.ui.max_mart_depth_input.setText(str(cfg.max_mart_depth))
        self.ui.mart_coef_input.setText(str(cfg.mart_coef))
        self.ui.pause_bars_num_input.setText(str(cfg.pause_bars))
        self.ui.min_delta_perc_input.setText(str(cfg.min_delta_perc))



    def deleteManagedSymbol(self, symbol=False):
        if symbol is False:
            symbol = self.sender().objectName().split("_")[0]

        strat = self.strat_manager.strategies.get(symbol)

        if strat and not strat.stopped:
            self.popError(f"Стратегия запущена, удаление невозможно")
            return

        #dataManager state for removal
        self.show_log(f"Removed managed symbol {symbol}")
        widget = self.managed_symbols_layouts[symbol]
        self.ui.configuredSymbolsVLayout.removeWidget(widget)
        widget.deleteLater()
        del self.managed_symbols_indicators[symbol]
        del self.managed_symbols_layouts[symbol]
        del self.strat_manager.symbols_cfg[symbol]
        self.updateTotalSymbols()


    def set_indicator_color(self, indicator, color):
        indicator.setStyleSheet("QRadioButton::indicator"
                                           "{"
                                           f"background-color : {color}"
                                           "}")

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
        start_btn.clicked.connect(self.start_single_strategy)
        rapid_stop_btn.clicked.connect(self.strat_manager.rapid_stop_single_strat)
        stop_updates_btn.clicked.connect(self.strat_manager.stop_single_strat)

        hbox.addWidget(radio_indicator)
        hbox.addWidget(symbol_btn)
        hbox.addWidget(delete_btn)
        hbox.addWidget(start_btn)
        hbox.addWidget(rapid_stop_btn)
        hbox.addWidget(stop_updates_btn)

        self.managed_symbols_indicators[symbol] = radio_indicator
        self.managed_symbols_layouts[symbol] = widget
        self.ui.configuredSymbolsVLayout.addWidget(widget)

    def start_single_strategy(self):
        if not self.check_uid():
            return
        symbol = self.sender().objectName().split("_")[0]
        self.strat_manager.init_strategy(symbol, True, self.on_strat_new_status)

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
        self.ui.direction_input.setCurrentIndex(0)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
#    widget.m_thread.quit()
    sys.exit(app.exec())
