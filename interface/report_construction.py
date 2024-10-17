from PySide6.QtCore import Qt, QAbstractTableModel, QObject, QDateTime, QTime, QDir
from PySide6.QtGui import QBrush
from PySide6.QtWidgets import QPushButton, QMainWindow, QHeaderView, QHBoxLayout, QWidget, QLabel, QDialog

from config_report_ui import Ui_Dialog as cfgReportUi
import db_connector
from datetime import datetime
import json


class ReportManager(QObject):
    def __init__(self, mainwindow):
        super().__init__()
        self.mainwindow = mainwindow
        self.current_report = None

        self.report_apply_last_day_period()
        self.mainwindow.ui.report_this_day_btn.clicked.connect(self.report_apply_last_day_period)
        self.mainwindow.ui.report_past_24h_btn.clicked.connect(self.report_apply_last_24h_period)
        self.mainwindow.ui.report_since_startup_btn.clicked.connect(self.report_apply_since_last_start_period)
        self.mainwindow.ui.report_show_report_btn.clicked.connect(self.show_deals_reports)
        self.mainwindow.ui.report_show_all_symbols_history_btn.clicked.connect(self.show_all_symbols_brief_report)

        self.ts_since = 0
        self.ts_till = 0
        self.symbol = ""
        self.config_widgets = {}
        self.cfg_report_windows = {}

    def show_all_symbols_brief_report(self):
        ts_since = None
        ts_till = None
        if "period" in self.sender().objectName():
            ts_since = self.mainwindow.ui.report_datetime_since_input.dateTime().toSecsSinceEpoch()
            ts_till = self.mainwindow.ui.report_datetime_till_input.dateTime().toSecsSinceEpoch()

        db_data = db_connector.get_symbols_general_info(ts_since, ts_till)
        parsed = []
        for symbol_data in db_data:
            dt_first = datetime.fromtimestamp(symbol_data[1]).strftime("%d/%m/%Y, %H:%M:%S")
            dt_last = datetime.fromtimestamp(symbol_data[2]).strftime("%d/%m/%Y, %H:%M:%S")
            parsed.append([symbol_data[0], dt_first, dt_last, symbol_data[3],
                           symbol_data[4], symbol_data[5], symbol_data[6],
                           symbol_data[7], symbol_data[8]])

        model = SymbolDealsBriefHistoryTableModel(parsed)
        self.mainwindow.ui.report_all_symbols_history_tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents);
        self.mainwindow.ui.report_all_symbols_history_tableView.setModel(model)

    def show_deals_reports(self, deals_reports=None, configs=None):
        self.ts_since = 0
        self.ts_till = 0
        self.symbol = ""
        if not deals_reports:
            self.ts_since = self.mainwindow.ui.report_datetime_since_input.dateTime().toSecsSinceEpoch()
            self.ts_till = self.mainwindow.ui.report_datetime_till_input.dateTime().toSecsSinceEpoch()

            self.symbol = self.mainwindow.ui.report_symbol_input.text()
            self.symbol = self.symbol.upper()
            if self.symbol == "":
                self.mainwindow.popError("Symbol can't be empty")

            self.deals_reports = self.load_deal_reports()
        else:
            self.mainwindow.popError("Backtest is not implemented")

        self.show_reports()

    def load_deal_reports(self):
        deals_reports = list(db_connector.get_symbol_deals(self.symbol,
                                                           self.ts_since,
                                                           self.ts_till))
        deals_reports.sort(key=lambda x: x[4])
        for report in deals_reports:
            report.append("")
        return deals_reports

    def show_reports(self):
        self.show_total_profit_reports()
        dt_since = datetime.fromtimestamp(self.ts_since).strftime("%d/%m/%y\n%H:%M")
        dt_till = datetime.fromtimestamp(self.ts_till).strftime("%d/%m/%y\n%H:%M")
        self.mainwindow.ui.deals_result_total_period_start.setText(dt_since)
        self.mainwindow.ui.deals_result_total_period_end.setText(dt_till)

        self.show_configs_report()

        model = FinishedDealsDataTableModel(self.deals_reports, is_live_deals=False)
        self.mainwindow.ui.report_brief_deal_data_tableView.setModel(model)
        self.deal_detailed_report_btn = []

        for i in range(len(self.deals_reports)):
            detail_report_btn = QPushButton("Details", objectName=f"details_btn {i}")
            detail_report_btn.clicked.connect(self.construct_deal_detailed_report)
            self.mainwindow.ui.report_brief_deal_data_tableView.setIndexWidget(model.index(i, len(model.header_labels)-1), detail_report_btn)
            self.deal_detailed_report_btn.append(detail_report_btn)

    def show_total_profit_reports(self):
        total_profit_report = db_connector.get_symbol_deals_stat(self.symbol,
                                                                self.ts_since,
                                                                self.ts_till)
        self.mainwindow.ui.deals_profit_out.setText(str(total_profit_report[0][0][0]))
        self.mainwindow.ui.deals_profit_total_out.setText(str(round(float(total_profit_report[0][0][1]), 2)))
        self.mainwindow.ui.deals_profit_total_perc_out.setText(str(round(float(total_profit_report[0][0][2]), 2)))

        self.mainwindow.ui.deals_loss_out.setText(str(total_profit_report[1][0][0]))
        self.mainwindow.ui.deals_loss_total_out.setText(str(round(float(total_profit_report[1][0][1]), 2)))
        self.mainwindow.ui.deals_loss_total_perc_out.setText(str(round(float(total_profit_report[1][0][2]), 2)))

        self.mainwindow.ui.deals_num_total_out.setText(str(total_profit_report[2][0][0]))
        self.mainwindow.ui.deals_result_total_out.setText(str(round(float(total_profit_report[2][0][1]), 2)))
        self.mainwindow.ui.deals_result_total_perc_out.setText(str(round(float(total_profit_report[2][0][2]), 2)))

    def show_configs_report(self):
        config_ids = set()
        for report in self.deals_reports:
            config_ids.add(report[0])
        
        while True:
            item = self.mainwindow.ui.report_cfgDetailsVLayout.takeAt(0)
            if item and item.widget():
                item.widget().deleteLater()
            else:
                break

        for config_id in config_ids:
            hbox = QHBoxLayout()
            widget = QWidget(objectName=f'cfg_{config_id}_btn_widget')
            widget.setLayout(hbox)

            symbol_lbl = QLabel(f"{config_id}", objectName=f'config_{config_id}_lbl')
            report_btn = QPushButton(f"Details", objectName=f'cfg_{config_id}_report_btn')
            report_btn.clicked.connect(self.create_detailed_config_report_window)

            hbox.addWidget(symbol_lbl)
            hbox.addWidget(report_btn)

            self.config_widgets[config_id] = widget
            self.mainwindow.ui.report_cfgDetailsVLayout.addWidget(widget)

    def construct_deal_detailed_report(self):
        deal_num = int(self.sender().objectName().split(" ")[1])
        deal_report = self.deals_reports[deal_num]

        deal_orders = db_connector.get_deal_orders(deal_report[0])
        model_end = FinishedOrderDataTableModel(deal_orders)
        self.mainwindow.ui.tp_deal_report_tableView.setModel(model_end)

    def create_detailed_config_report_window(self):
        config_id = int(self.sender().objectName().split("_")[1])
        report_window = self.cfg_report_windows.get(config_id)
        config_data = db_connector.get_config(config_id)
        cfg = json.loads(config_data[1])
        if report_window is None:
            report_window = QDialog()
            report_window.ui = cfgReportUi()
            report_window.ui.setupUi(report_window)
            report_window.setWindowTitle(f"Details Config {config_id}")
            report_window.ui.close_window_btn.clicked.connect(report_window.close)

            report_window.ui.leverage_input.setText(str(cfg["leverage"]))
            report_window.ui.deal_deposit_input.setText(str(cfg["deal_deposit"]))
            report_window.ui.margin_type_input.setCurrentIndex(cfg["margin_type_index"])
            if cfg["allowed_direction"] != -1:
                report_window.ui.allowed_direction_input.setCurrentIndex(cfg["allowed_direction"])
            else:
                report_window.ui.allowed_direction_input.setCurrentIndex(2)
            report_window.ui.tp_input.setText(str(cfg["tp"]))
            if cfg["sl"] is not None:
                report_window.ui.sl_input.setText(str(cfg["sl"]))
            else:
                report_window.ui.sl_input.setText("")
            if cfg["ema_cross_tp"] is not None:
                report_window.ui.ema_cross_tp_input.setText(str(cfg["ema_cross_tp"]))

            report_window.ui.tf_input.setCurrentIndex(cfg["tf_index"])
            report_window.ui.slow_ema_period_input.setText(str(cfg["ema_slow"]))
            report_window.ui.fast_ema_period_input.setText(str(cfg["ema_fast"]))
            report_window.ui.max_mart_depth_input.setText(str(cfg["max_mart_depth"]))
            report_window.ui.mart_coef_input.setText(str(cfg["mart_coef"]))
            report_window.ui.pause_bars_num_input.setText(str(cfg["pause_bars"]))
            report_window.ui.min_delta_perc_input.setText(str(cfg["min_delta_perc"]))

            if cfg["f_enabled"]:
                report_window.ui.filter_enabled_chkbx.setChecked(True)
            else:
                report_window.ui.filter_enabled_chkbx.setChecked(False)
            
            if cfg.get("f_add_pos_disabled"):
                report_window.ui.filter_disable_position_add_chkbx.setChecked(True)
            else:
                report_window.ui.filter_disable_position_add_chkbx.setChecked(False)

            report_window.ui.filter_slow_ema_period_input.setText(str(cfg["f_ema_slow"]) if cfg["f_ema_slow"] else "")
            report_window.ui.filter_fast_ema_period_input.setText(str(cfg["f_ema_fast"]) if cfg["f_ema_fast"] else "")
            report_window.ui.filter_delta_limit.setText(str(cfg["f_max_allowed_delta"]) if cfg["f_max_allowed_delta"] else "")
            report_window.ui.filter_tf_input.setCurrentIndex(cfg["f_tf_index"])
            
            try:
                first_deal_deposit = float(cfg["deal_deposit"])
                addition_orders_num = int(cfg["max_mart_depth"])
                mart_coef = float(cfg["mart_coef"])

                if mart_coef != "" and addition_orders_num != "" and first_deal_deposit != "":
                    last_deal_deposit = float(first_deal_deposit)
                    max_deal_deposit = last_deal_deposit
                    mart_coef = float(mart_coef)/100 + 1
                    addition_orders_num = int(float(addition_orders_num))
                    
                    for _ in range(1, addition_orders_num+1):
                        last_deal_deposit *= mart_coef
                        max_deal_deposit += last_deal_deposit

                    max_deal_deposit = int(max_deal_deposit)
                    report_window.ui.max_deal_deposit.setText(str(max_deal_deposit))
                else:
                    report_window.ui.max_deal_deposit.setText("")
            except:
                pass

            self.cfg_report_windows[config_id] = report_window

        report_window.show()

    def report_apply_last_24h_period(self):
        now = QDateTime.currentDateTime()
        prev_day = now.addDays(-1)
        self.mainwindow.ui.report_datetime_since_input.setDateTime(prev_day)
        self.mainwindow.ui.report_datetime_till_input.setDateTime(now)

    def report_apply_last_day_period(self):
        today = QDateTime.currentDateTime()
        today.setTime(QTime(0,0,0))
        self.mainwindow.ui.report_datetime_since_input.setDateTime(today)
        self.mainwindow.ui.report_datetime_till_input.setDateTime(QDateTime.currentDateTime())

    def report_apply_since_last_start_period(self):
        dt_start = QDateTime()
        dt_start.setSecsSinceEpoch(self.mainwindow.ts_start)

        self.mainwindow.ui.report_datetime_since_input.setDateTime(dt_start)
        self.mainwindow.ui.report_datetime_till_input.setDateTime(QDateTime.currentDateTime())


class RunningDealsDataTableModel(QAbstractTableModel):
    def __init__(self, data):
        super(RunningDealsDataTableModel, self).__init__()
        self.header_labels = ["Инструмент", "Направление", "Плечо", "ТФ(мин)",
                              "Вложено $", "Сред. Цена", "Докупок", "Время Открытия"]
        self._data = data

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        if len(self._data) > 0:
            return len(self._data[0])
        else:
            return 0

class FinishedDealsDataTableModel(QAbstractTableModel):
    def __init__(self, data, is_live_deals=True):
        super(FinishedDealsDataTableModel, self).__init__()
        self.header_labels = ["Конфиг", "Инструмент", "Направление", "Размер", "Докупок",
                              "Комиссия", "Результат", "Результат %", "Начало", "Конец"]

        self._data = data
        self.is_live_deals = is_live_deals
        if not is_live_deals:
            self.header_labels.append("Подробно")

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def data(self, index, role):

        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            if (index.column() > len(self.header_labels)) and not self.is_live_deals:
                return
            
            return self._data[index.row()][index.column()]

        if role == Qt.BackgroundRole:
            if index.column() == 6: #results
                data = self._data[index.row()][index.column()]
                color = QBrush(Qt.lightGray)
                if data < 0:
                    color = QBrush(Qt.red)
                elif data > 0:
                    color = QBrush(Qt.green)
                return color

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self.header_labels)

class FinishedOrderDataTableModel(QAbstractTableModel):
    def __init__(self, data, is_live_deals=True):
        super(FinishedOrderDataTableModel, self).__init__()
        self.header_labels = ["Инструмент", "Тип", "Направление", "Монет", "Цена", "Сумма $", 
                              "Комиссия", "Время Исполнения"]
        
        self._data = data

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def data(self, index, role):
        
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]


    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self.header_labels)

class SymbolDealsBriefHistoryTableModel(QAbstractTableModel):
    def __init__(self, data):
        super(SymbolDealsBriefHistoryTableModel, self).__init__()
        self.header_labels = ["Символ", "Дата 1й\nсделки", "Дата последней\nсделки",
                              "Всего сделок", "В плюс", "В минус",
                              "Итог", "Всего плюс", "Всего минус"]
        self._data = data

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        if len(self._data) > 0:
            return len(self._data[0])
        else:
            return 0








# from PySide6.QtCore import Qt, QAbstractTableModel
# from PySide6.QtGui import QBrush

# class FinishedDealsDataTableModel(QAbstractTableModel):
#     def __init__(self, data, is_live_deals=True):
#         super(FinishedDealsDataTableModel, self).__init__()
#         self.header_labels = ["Инструмент", "ТФ", "Направление", "Плечо", "Начало", "Окончание",
#                               "Позиция $", "Докупок", "Результат", "Результат %", "Коммиссия"]

#         if not is_live_deals:
#             self.header_labels.append("Конфиг")
#             self.header_labels.append("Детали")
#         self._data = data
#         self.last_cfg_num = None

#     def headerData(self, section, orientation, role=Qt.DisplayRole):
#         if role == Qt.DisplayRole and orientation == Qt.Horizontal:
#             return self.header_labels[section]
#         return QAbstractTableModel.headerData(self, section, orientation, role)

#     def data(self, index, role):

#         if role == Qt.DisplayRole:
#             # See below for the nested-list data structure.
#             # .row() indexes into the outer list,
#             # .column() indexes into the sub-list
#             return self._data[index.row()][index.column()]

#         if role == Qt.BackgroundRole:
#             if index.column() == 8: #results
#                 data = self._data[index.row()][index.column()]
#                 color = QBrush(Qt.lightGray)
#                 if data < 0:
#                     color = QBrush(Qt.red)
#                 elif data > 0:
#                     color = QBrush(Qt.green)
#                 return color

#     def rowCount(self, index):
#         # The length of the outer list.
#         return len(self._data)

#     def columnCount(self, index):
#         # The following takes the first sub-list, and returns
#         # the length (only works if all rows are an equal length)
#         return len(self.header_labels)

