# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTableView,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1044, 827)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_12 = QGridLayout(self.centralwidget)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tab_general = QWidget()
        self.tab_general.setObjectName(u"tab_general")
        self.gridLayout_5 = QGridLayout(self.tab_general)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.rapid_stop_all_btn = QPushButton(self.tab_general)
        self.rapid_stop_all_btn.setObjectName(u"rapid_stop_all_btn")
        self.rapid_stop_all_btn.setStyleSheet(u"background: rgb(237, 51, 59);\n"
"font: 11pt \"Cantarell\";\n"
"color:  rgb(0, 0, 0); ")

        self.gridLayout_5.addWidget(self.rapid_stop_all_btn, 2, 0, 1, 1)

        self.stop_all_btn = QPushButton(self.tab_general)
        self.stop_all_btn.setObjectName(u"stop_all_btn")

        self.gridLayout_5.addWidget(self.stop_all_btn, 1, 0, 1, 1)

        self.refresh_open_deals_btn = QPushButton(self.tab_general)
        self.refresh_open_deals_btn.setObjectName(u"refresh_open_deals_btn")

        self.gridLayout_5.addWidget(self.refresh_open_deals_btn, 3, 1, 1, 1)

        self.refresh_finished_deals_btn = QPushButton(self.tab_general)
        self.refresh_finished_deals_btn.setObjectName(u"refresh_finished_deals_btn")

        self.gridLayout_5.addWidget(self.refresh_finished_deals_btn, 5, 1, 1, 1)

        self.logger_lbl = QLabel(self.tab_general)
        self.logger_lbl.setObjectName(u"logger_lbl")

        self.gridLayout_5.addWidget(self.logger_lbl, 8, 0, 1, 1)

        self.label = QLabel(self.tab_general)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 3, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.depo_start_val = QLabel(self.tab_general)
        self.depo_start_val.setObjectName(u"depo_start_val")
        self.depo_start_val.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.depo_start_val, 1, 1, 1, 1)

        self.tss_lbl = QLabel(self.tab_general)
        self.tss_lbl.setObjectName(u"tss_lbl")

        self.gridLayout_4.addWidget(self.tss_lbl, 0, 0, 1, 1)

        self.depo_current_lbl = QLabel(self.tab_general)
        self.depo_current_lbl.setObjectName(u"depo_current_lbl")

        self.gridLayout_4.addWidget(self.depo_current_lbl, 2, 0, 1, 1)

        self.depo_current_val = QLabel(self.tab_general)
        self.depo_current_val.setObjectName(u"depo_current_val")
        self.depo_current_val.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.depo_current_val, 2, 1, 1, 1)

        self.depo_start_lbl = QLabel(self.tab_general)
        self.depo_start_lbl.setObjectName(u"depo_start_lbl")

        self.gridLayout_4.addWidget(self.depo_start_lbl, 1, 0, 1, 1)

        self.tss_val = QLabel(self.tab_general)
        self.tss_val.setObjectName(u"tss_val")
        self.tss_val.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.tss_val, 0, 1, 1, 1)

        self.depo_delta_lbl = QLabel(self.tab_general)
        self.depo_delta_lbl.setObjectName(u"depo_delta_lbl")

        self.gridLayout_4.addWidget(self.depo_delta_lbl, 3, 0, 1, 1)

        self.depo_delta_val = QLabel(self.tab_general)
        self.depo_delta_val.setObjectName(u"depo_delta_val")
        self.depo_delta_val.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.depo_delta_val, 3, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 1, 3, 1)

        self.finished_deals_lbl = QLabel(self.tab_general)
        self.finished_deals_lbl.setObjectName(u"finished_deals_lbl")

        self.gridLayout_5.addWidget(self.finished_deals_lbl, 5, 0, 1, 1)

        self.finished_deals_table = QTableView(self.tab_general)
        self.finished_deals_table.setObjectName(u"finished_deals_table")

        self.gridLayout_5.addWidget(self.finished_deals_table, 6, 0, 1, 2)

        self.start_all_btn = QPushButton(self.tab_general)
        self.start_all_btn.setObjectName(u"start_all_btn")
        self.start_all_btn.setStyleSheet(u"background: rgb(143, 240, 164);\n"
"font: 11pt \"Cantarell\";\n"
"color:  rgb(0, 0, 0);")

        self.gridLayout_5.addWidget(self.start_all_btn, 0, 0, 1, 1)

        self.logger_field = QTextBrowser(self.tab_general)
        self.logger_field.setObjectName(u"logger_field")

        self.gridLayout_5.addWidget(self.logger_field, 9, 0, 1, 2)

        self.open_deals_table = QTableView(self.tab_general)
        self.open_deals_table.setObjectName(u"open_deals_table")

        self.gridLayout_5.addWidget(self.open_deals_table, 4, 0, 1, 2)

        self.tabWidget.addTab(self.tab_general, "")
        self.tab_settings = QWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        self.gridLayout_3 = QGridLayout(self.tab_settings)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.load_cfg_btn = QPushButton(self.tab_settings)
        self.load_cfg_btn.setObjectName(u"load_cfg_btn")

        self.gridLayout_3.addWidget(self.load_cfg_btn, 0, 1, 1, 1)

        self.label_5 = QLabel(self.tab_settings)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)

        self.configuredSymbolsScrollArea = QScrollArea(self.tab_settings)
        self.configuredSymbolsScrollArea.setObjectName(u"configuredSymbolsScrollArea")
        self.configuredSymbolsScrollArea.setWidgetResizable(True)
        self.configuredSymbolsScrollAreaWidget = QWidget()
        self.configuredSymbolsScrollAreaWidget.setObjectName(u"configuredSymbolsScrollAreaWidget")
        self.configuredSymbolsScrollAreaWidget.setGeometry(QRect(0, 0, 497, 613))
        self.verticalLayout = QVBoxLayout(self.configuredSymbolsScrollAreaWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.configuredSymbolsVLayout = QVBoxLayout()
        self.configuredSymbolsVLayout.setObjectName(u"configuredSymbolsVLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.configuredSymbolsVLayout.addItem(self.verticalSpacer)


        self.verticalLayout.addLayout(self.configuredSymbolsVLayout)

        self.configuredSymbolsScrollArea.setWidget(self.configuredSymbolsScrollAreaWidget)

        self.gridLayout_3.addWidget(self.configuredSymbolsScrollArea, 2, 0, 6, 1)

        self.save_cfg_btn = QPushButton(self.tab_settings)
        self.save_cfg_btn.setObjectName(u"save_cfg_btn")

        self.gridLayout_3.addWidget(self.save_cfg_btn, 1, 1, 1, 1)

        self.header_3 = QLabel(self.tab_settings)
        self.header_3.setObjectName(u"header_3")

        self.gridLayout_3.addWidget(self.header_3, 2, 1, 1, 1)

        self.clean_input_btn = QPushButton(self.tab_settings)
        self.clean_input_btn.setObjectName(u"clean_input_btn")

        self.gridLayout_3.addWidget(self.clean_input_btn, 8, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tp1_lbl = QLabel(self.tab_settings)
        self.tp1_lbl.setObjectName(u"tp1_lbl")

        self.gridLayout_2.addWidget(self.tp1_lbl, 2, 0, 1, 1)

        self.tp_input = QLineEdit(self.tab_settings)
        self.tp_input.setObjectName(u"tp_input")

        self.gridLayout_2.addWidget(self.tp_input, 2, 1, 1, 1)

        self.sl_input = QLineEdit(self.tab_settings)
        self.sl_input.setObjectName(u"sl_input")

        self.gridLayout_2.addWidget(self.sl_input, 1, 1, 1, 1)

        self.rp_lbl = QLabel(self.tab_settings)
        self.rp_lbl.setObjectName(u"rp_lbl")
        self.rp_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.rp_lbl, 0, 1, 1, 1)

        self.sl_lbl = QLabel(self.tab_settings)
        self.sl_lbl.setObjectName(u"sl_lbl")

        self.gridLayout_2.addWidget(self.sl_lbl, 1, 0, 1, 1)

        self.ema_cross_close_lbl = QLabel(self.tab_settings)
        self.ema_cross_close_lbl.setObjectName(u"ema_cross_close_lbl")

        self.gridLayout_2.addWidget(self.ema_cross_close_lbl, 3, 0, 1, 1)

        self.ema_cross_tp_input = QLineEdit(self.tab_settings)
        self.ema_cross_tp_input.setObjectName(u"ema_cross_tp_input")

        self.gridLayout_2.addWidget(self.ema_cross_tp_input, 3, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)

        self.gridLayout_3.addLayout(self.gridLayout_2, 6, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.total_symbols = QLabel(self.tab_settings)
        self.total_symbols.setObjectName(u"total_symbols")

        self.horizontalLayout_2.addWidget(self.total_symbols)

        self.total_symbols_val = QLabel(self.tab_settings)
        self.total_symbols_val.setObjectName(u"total_symbols_val")

        self.horizontalLayout_2.addWidget(self.total_symbols_val)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 8, 0, 1, 1)

        self.add_asset_cfg_btn = QPushButton(self.tab_settings)
        self.add_asset_cfg_btn.setObjectName(u"add_asset_cfg_btn")

        self.gridLayout_3.addWidget(self.add_asset_cfg_btn, 7, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.margin_type_lbl = QLabel(self.tab_settings)
        self.margin_type_lbl.setObjectName(u"margin_type_lbl")

        self.gridLayout.addWidget(self.margin_type_lbl, 4, 0, 1, 1)

        self.direction_lbl = QLabel(self.tab_settings)
        self.direction_lbl.setObjectName(u"direction_lbl")

        self.gridLayout.addWidget(self.direction_lbl, 5, 0, 1, 1)

        self.slow_ema_period_input = QLineEdit(self.tab_settings)
        self.slow_ema_period_input.setObjectName(u"slow_ema_period_input")

        self.gridLayout.addWidget(self.slow_ema_period_input, 6, 1, 1, 1)

        self.slow_ema_period_lbl = QLabel(self.tab_settings)
        self.slow_ema_period_lbl.setObjectName(u"slow_ema_period_lbl")
        self.slow_ema_period_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.slow_ema_period_lbl, 6, 0, 1, 1)

        self.min_delta_perc_lbl = QLabel(self.tab_settings)
        self.min_delta_perc_lbl.setObjectName(u"min_delta_perc_lbl")

        self.gridLayout.addWidget(self.min_delta_perc_lbl, 11, 0, 1, 1)

        self.margin_type_input = QComboBox(self.tab_settings)
        self.margin_type_input.addItem("")
        self.margin_type_input.addItem("")
        self.margin_type_input.setObjectName(u"margin_type_input")

        self.gridLayout.addWidget(self.margin_type_input, 4, 1, 1, 1)

        self.min_delta_perc_input = QLineEdit(self.tab_settings)
        self.min_delta_perc_input.setObjectName(u"min_delta_perc_input")

        self.gridLayout.addWidget(self.min_delta_perc_input, 11, 1, 1, 1)

        self.pause_bars_num_input = QLineEdit(self.tab_settings)
        self.pause_bars_num_input.setObjectName(u"pause_bars_num_input")

        self.gridLayout.addWidget(self.pause_bars_num_input, 10, 1, 1, 1)

        self.max_mart_depth_input = QLineEdit(self.tab_settings)
        self.max_mart_depth_input.setObjectName(u"max_mart_depth_input")

        self.gridLayout.addWidget(self.max_mart_depth_input, 8, 1, 1, 1)

        self.deal_deposit_input = QLineEdit(self.tab_settings)
        self.deal_deposit_input.setObjectName(u"deal_deposit_input")

        self.gridLayout.addWidget(self.deal_deposit_input, 3, 1, 1, 1)

        self.leverage_lbl = QLabel(self.tab_settings)
        self.leverage_lbl.setObjectName(u"leverage_lbl")

        self.gridLayout.addWidget(self.leverage_lbl, 2, 0, 1, 1)

        self.fast_ema_period_lbl = QLabel(self.tab_settings)
        self.fast_ema_period_lbl.setObjectName(u"fast_ema_period_lbl")
        self.fast_ema_period_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.fast_ema_period_lbl, 7, 0, 1, 1)

        self.pause_bars_num_lbl = QLabel(self.tab_settings)
        self.pause_bars_num_lbl.setObjectName(u"pause_bars_num_lbl")

        self.gridLayout.addWidget(self.pause_bars_num_lbl, 10, 0, 1, 1)

        self.asset_lbl = QLabel(self.tab_settings)
        self.asset_lbl.setObjectName(u"asset_lbl")

        self.gridLayout.addWidget(self.asset_lbl, 0, 0, 1, 1)

        self.tf_lbl = QLabel(self.tab_settings)
        self.tf_lbl.setObjectName(u"tf_lbl")

        self.gridLayout.addWidget(self.tf_lbl, 1, 0, 1, 1)

        self.tf_input = QComboBox(self.tab_settings)
        self.tf_input.addItem("")
        self.tf_input.addItem("")
        self.tf_input.addItem("")
        self.tf_input.addItem("")
        self.tf_input.addItem("")
        self.tf_input.addItem("")
        self.tf_input.addItem("")
        self.tf_input.addItem("")
        self.tf_input.addItem("")
        self.tf_input.setObjectName(u"tf_input")

        self.gridLayout.addWidget(self.tf_input, 1, 1, 1, 1)

        self.fast_ema_period_input = QLineEdit(self.tab_settings)
        self.fast_ema_period_input.setObjectName(u"fast_ema_period_input")

        self.gridLayout.addWidget(self.fast_ema_period_input, 7, 1, 1, 1)

        self.max_mart_depth_lbl = QLabel(self.tab_settings)
        self.max_mart_depth_lbl.setObjectName(u"max_mart_depth_lbl")
        self.max_mart_depth_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.max_mart_depth_lbl, 8, 0, 1, 1)

        self.leverage_input = QLineEdit(self.tab_settings)
        self.leverage_input.setObjectName(u"leverage_input")

        self.gridLayout.addWidget(self.leverage_input, 2, 1, 1, 1)

        self.symbol_input = QLineEdit(self.tab_settings)
        self.symbol_input.setObjectName(u"symbol_input")
        self.symbol_input.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.symbol_input, 0, 1, 1, 1)

        self.deal_deposit_lbl = QLabel(self.tab_settings)
        self.deal_deposit_lbl.setObjectName(u"deal_deposit_lbl")

        self.gridLayout.addWidget(self.deal_deposit_lbl, 3, 0, 1, 1)

        self.allowed_direction_input = QComboBox(self.tab_settings)
        self.allowed_direction_input.addItem("")
        self.allowed_direction_input.addItem("")
        self.allowed_direction_input.addItem("")
        self.allowed_direction_input.setObjectName(u"allowed_direction_input")

        self.gridLayout.addWidget(self.allowed_direction_input, 5, 1, 1, 1)

        self.mart_coef_input = QLineEdit(self.tab_settings)
        self.mart_coef_input.setObjectName(u"mart_coef_input")

        self.gridLayout.addWidget(self.mart_coef_input, 9, 1, 1, 1)

        self.mart_coef_lbl = QLabel(self.tab_settings)
        self.mart_coef_lbl.setObjectName(u"mart_coef_lbl")

        self.gridLayout.addWidget(self.mart_coef_lbl, 9, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.gridLayout_3.addLayout(self.gridLayout, 4, 1, 1, 1)

        self.header_2 = QLabel(self.tab_settings)
        self.header_2.setObjectName(u"header_2")
        self.header_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.header_2, 5, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.max_simultaneous_deals_lbl = QLabel(self.tab_settings)
        self.max_simultaneous_deals_lbl.setObjectName(u"max_simultaneous_deals_lbl")

        self.horizontalLayout.addWidget(self.max_simultaneous_deals_lbl)

        self.max_simultaneous_deals_input = QLineEdit(self.tab_settings)
        self.max_simultaneous_deals_input.setObjectName(u"max_simultaneous_deals_input")

        self.horizontalLayout.addWidget(self.max_simultaneous_deals_input)

        self.max_simultaneous_deals_btn = QPushButton(self.tab_settings)
        self.max_simultaneous_deals_btn.setObjectName(u"max_simultaneous_deals_btn")

        self.horizontalLayout.addWidget(self.max_simultaneous_deals_btn)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_settings, "")

        self.gridLayout_12.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1044, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.rapid_stop_all_btn.setText(QCoreApplication.translate("MainWindow", u"Market Stop All", None))
        self.stop_all_btn.setText(QCoreApplication.translate("MainWindow", u"Stop New Signals", None))
        self.refresh_open_deals_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.refresh_finished_deals_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.logger_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0431\u044b\u0442\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b \u0441\u0442\u0440\u0430\u0442\u0435\u0433\u0438\u0439:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044b\u0435 \u043f\u043e\u0437\u0438\u0446\u0438\u0438", None))
        self.depo_start_val.setText("")
        self.tss_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0441 \u043c\u043e\u043c\u0435\u043d\u0442\u0430 \u0437\u0430\u043f\u0443\u0441\u043a\u0430: ", None))
        self.depo_current_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0434\u0435\u043f\u043e\u0437\u0438\u0442:", None))
        self.depo_current_val.setText("")
        self.depo_start_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043f\u043e\u0437\u0438\u0442 \u043d\u0430 \u043c\u043e\u043c\u0435\u043d\u0442 \u0437\u0430\u043f\u0443\u0441\u043a\u0430:  ", None))
        self.tss_val.setText("")
        self.depo_delta_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0434\u0435\u043f\u043e\u0437\u0438\u0442\u0430:", None))
        self.depo_delta_val.setText("")
        self.finished_deals_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043d\u044b\u0435 \u0441\u0434\u0435\u043b\u043a\u0438", None))
        self.start_all_btn.setText(QCoreApplication.translate("MainWindow", u"Start All", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.load_cfg_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044e", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u044b\u0435 \u0410\u043a\u0442\u0438\u0432\u044b", None))
        self.save_cfg_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0442\u0435\u043a\u0443\u0449\u0443\u044e \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044e", None))
        self.header_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0435\u043c\u0435\u0442\u0440\u044b \u0432\u0445\u043e\u0434\u0430 \u0432 \u0441\u0434\u0435\u043b\u043a\u0443:", None))
        self.clean_input_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0432\u0432\u043e\u0434", None))
        self.tp1_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0422\u041f", None))
        self.rp_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (%)", None))
        self.sl_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043f", None))
        self.ema_cross_close_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434 EMA CROSS", None))
        self.ema_cross_tp_input.setInputMask("")
        self.ema_cross_tp_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d. % \u0434\u043b\u044f \u043e\u0442\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
        self.total_symbols.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435\u0433\u043e \u043f\u0430\u0440:", None))
        self.total_symbols_val.setText("")
        self.add_asset_cfg_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.margin_type_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u041c\u0430\u0440\u0436\u0438", None))
        self.direction_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.slow_ema_period_input.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.slow_ema_period_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u041c\u0435\u0434\u043b\u0435\u043d\u043d\u043e\u0439\n"
"\u0415\u041c\u0410 (\u0431\u0430\u0440\u043e\u0432)", None))
        self.min_delta_perc_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d. \u0414\u0435\u043b\u044c\u0442\u0430 \u0434\u043e\u043a\u0443\u043f\u0430, %", None))
        self.margin_type_input.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u043b\u0435\u0439\u0442", None))
        self.margin_type_input.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041a\u0440\u043e\u0441\u0441", None))

        self.min_delta_perc_input.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pause_bars_num_input.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.max_mart_depth_input.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.deal_deposit_input.setInputMask("")
        self.leverage_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0435\u0447\u043e", None))
        self.fast_ema_period_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0411\u044b\u0441\u0442\u0440\u043e\u0439\n"
"\u0415\u041c\u0410 (\u0431\u0430\u0440\u043e\u0432)", None))
        self.pause_bars_num_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0443\u0437\u0430, \u043a\u043e\u043b-\u0432\u043e \u0411\u0430\u0440\u043e\u0432", None))
        self.asset_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432", None))
        self.tf_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0444\u0440\u0435\u0439\u043c", None))
        self.tf_input.setItemText(0, QCoreApplication.translate("MainWindow", u"1m", None))
        self.tf_input.setItemText(1, QCoreApplication.translate("MainWindow", u"3m", None))
        self.tf_input.setItemText(2, QCoreApplication.translate("MainWindow", u"5m", None))
        self.tf_input.setItemText(3, QCoreApplication.translate("MainWindow", u"15m", None))
        self.tf_input.setItemText(4, QCoreApplication.translate("MainWindow", u"30m", None))
        self.tf_input.setItemText(5, QCoreApplication.translate("MainWindow", u"1h", None))
        self.tf_input.setItemText(6, QCoreApplication.translate("MainWindow", u"4h", None))
        self.tf_input.setItemText(7, QCoreApplication.translate("MainWindow", u"6h", None))
        self.tf_input.setItemText(8, QCoreApplication.translate("MainWindow", u"12h", None))

        self.fast_ema_period_input.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.max_mart_depth_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0441\n"
"\u0413\u043b\u0443\u0431\u0438\u043d\u0430 \u041c\u0430\u0440\u0442\u0438\u043d\u0433\u0435\u0439\u043b", None))
        self.leverage_input.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.deal_deposit_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 1 \u0412\u0445\u043e\u0434\u0430\n"
"(\u0431\u0435\u0437 \u0443\u0447\u0451\u0442\u0430 \u043f\u043b\u0435\u0447\u0430)", None))
        self.allowed_direction_input.setItemText(0, QCoreApplication.translate("MainWindow", u"BOTH", None))
        self.allowed_direction_input.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u044c\u043a\u043e LONG", None))
        self.allowed_direction_input.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u044c\u043a\u043e SHORT", None))

        self.mart_coef_input.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.mart_coef_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u0438\u0435 \u043f\u0440\u0438 \u041c\u0430\u0440\u0442\u0438\u043d\u0433\u0435\u0439\u043b, %", None))
        self.header_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0435\u043c\u0435\u0442\u0440\u044b \u0432\u044b\u0445\u043e\u0434\u0430 \u0438\u0437 \u0441\u0434\u0435\u043b\u043a\u0438", None))
        self.max_simultaneous_deals_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0434\u0435\u043b\u043e\u043a \u043e\u0434\u043d\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e (\u043c\u0430\u043a\u0441 10)", None))
        self.max_simultaneous_deals_input.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.max_simultaneous_deals_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
    # retranslateUi

