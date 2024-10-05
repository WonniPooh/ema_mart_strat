# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTableView, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1240, 838)
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
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.load_cfg_btn = QPushButton(self.tab_settings)
        self.load_cfg_btn.setObjectName(u"load_cfg_btn")

        self.verticalLayout_2.addWidget(self.load_cfg_btn)

        self.save_cfg_btn = QPushButton(self.tab_settings)
        self.save_cfg_btn.setObjectName(u"save_cfg_btn")
        self.save_cfg_btn.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.save_cfg_btn)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 3, 1, 1)

        self.gridFrame = QFrame(self.tab_settings)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setFrameShape(QFrame.Box)
        self.gridLayout_7 = QGridLayout(self.gridFrame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.filter_delta_limit = QLineEdit(self.gridFrame)
        self.filter_delta_limit.setObjectName(u"filter_delta_limit")

        self.gridLayout_7.addWidget(self.filter_delta_limit, 5, 1, 1, 1)

        self.label_11 = QLabel(self.gridFrame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_7.addWidget(self.label_11, 1, 0, 1, 1)

        self.filter_slow_ema_period_input = QLineEdit(self.gridFrame)
        self.filter_slow_ema_period_input.setObjectName(u"filter_slow_ema_period_input")

        self.gridLayout_7.addWidget(self.filter_slow_ema_period_input, 3, 1, 1, 1)

        self.label_8 = QLabel(self.gridFrame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_7.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_7 = QLabel(self.gridFrame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_7.addWidget(self.label_7, 2, 0, 1, 1)

        self.filter_tf_input = QComboBox(self.gridFrame)
        self.filter_tf_input.addItem("")
        self.filter_tf_input.addItem("")
        self.filter_tf_input.addItem("")
        self.filter_tf_input.addItem("")
        self.filter_tf_input.addItem("")
        self.filter_tf_input.addItem("")
        self.filter_tf_input.addItem("")
        self.filter_tf_input.addItem("")
        self.filter_tf_input.addItem("")
        self.filter_tf_input.setObjectName(u"filter_tf_input")

        self.gridLayout_7.addWidget(self.filter_tf_input, 2, 1, 1, 1)

        self.filter_enabled_chkbx = QCheckBox(self.gridFrame)
        self.filter_enabled_chkbx.setObjectName(u"filter_enabled_chkbx")
        self.filter_enabled_chkbx.setLayoutDirection(Qt.LeftToRight)
        self.filter_enabled_chkbx.setStyleSheet(u"margin-left:50%; \n"
"margin-right:50%;")

        self.gridLayout_7.addWidget(self.filter_enabled_chkbx, 1, 1, 1, 1)

        self.filter_fast_ema_period_input = QLineEdit(self.gridFrame)
        self.filter_fast_ema_period_input.setObjectName(u"filter_fast_ema_period_input")

        self.gridLayout_7.addWidget(self.filter_fast_ema_period_input, 4, 1, 1, 1)

        self.label_10 = QLabel(self.gridFrame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_7.addWidget(self.label_10, 5, 0, 1, 1)

        self.label_9 = QLabel(self.gridFrame)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_7.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_6 = QLabel(self.gridFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 2)

        self.gridLayout_7.setRowStretch(0, 1)
        self.gridLayout_7.setColumnStretch(0, 2)

        self.gridLayout_3.addWidget(self.gridFrame, 3, 3, 1, 1)

        self.configuredSymbolsScrollArea = QScrollArea(self.tab_settings)
        self.configuredSymbolsScrollArea.setObjectName(u"configuredSymbolsScrollArea")
        self.configuredSymbolsScrollArea.setWidgetResizable(True)
        self.configuredSymbolsScrollAreaWidget = QWidget()
        self.configuredSymbolsScrollAreaWidget.setObjectName(u"configuredSymbolsScrollAreaWidget")
        self.configuredSymbolsScrollAreaWidget.setGeometry(QRect(0, 0, 477, 526))
        self.verticalLayout = QVBoxLayout(self.configuredSymbolsScrollAreaWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.configuredSymbolsVLayout = QVBoxLayout()
        self.configuredSymbolsVLayout.setObjectName(u"configuredSymbolsVLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.configuredSymbolsVLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.total_symbols = QLabel(self.configuredSymbolsScrollAreaWidget)
        self.total_symbols.setObjectName(u"total_symbols")

        self.horizontalLayout_2.addWidget(self.total_symbols)

        self.total_symbols_val = QLabel(self.configuredSymbolsScrollAreaWidget)
        self.total_symbols_val.setObjectName(u"total_symbols_val")

        self.horizontalLayout_2.addWidget(self.total_symbols_val)


        self.configuredSymbolsVLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.configuredSymbolsVLayout)

        self.configuredSymbolsScrollArea.setWidget(self.configuredSymbolsScrollAreaWidget)

        self.gridLayout_3.addWidget(self.configuredSymbolsScrollArea, 3, 0, 4, 2)

        self.frame = QFrame(self.tab_settings)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tf_input = QComboBox(self.frame)
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

        self.gridLayout.addWidget(self.tf_input, 3, 1, 1, 1)

        self.max_mart_depth_lbl = QLabel(self.frame)
        self.max_mart_depth_lbl.setObjectName(u"max_mart_depth_lbl")
        self.max_mart_depth_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.max_mart_depth_lbl, 11, 0, 1, 1)

        self.deal_deposit_input = QLineEdit(self.frame)
        self.deal_deposit_input.setObjectName(u"deal_deposit_input")

        self.gridLayout.addWidget(self.deal_deposit_input, 5, 1, 1, 1)

        self.slow_ema_period_input = QLineEdit(self.frame)
        self.slow_ema_period_input.setObjectName(u"slow_ema_period_input")

        self.gridLayout.addWidget(self.slow_ema_period_input, 9, 1, 1, 1)

        self.pause_bars_num_input = QLineEdit(self.frame)
        self.pause_bars_num_input.setObjectName(u"pause_bars_num_input")

        self.gridLayout.addWidget(self.pause_bars_num_input, 13, 1, 1, 1)

        self.allowed_direction_input = QComboBox(self.frame)
        self.allowed_direction_input.addItem("")
        self.allowed_direction_input.addItem("")
        self.allowed_direction_input.addItem("")
        self.allowed_direction_input.setObjectName(u"allowed_direction_input")

        self.gridLayout.addWidget(self.allowed_direction_input, 8, 1, 1, 1)

        self.min_delta_perc_input = QLineEdit(self.frame)
        self.min_delta_perc_input.setObjectName(u"min_delta_perc_input")

        self.gridLayout.addWidget(self.min_delta_perc_input, 14, 1, 1, 1)

        self.header_3 = QLabel(self.frame)
        self.header_3.setObjectName(u"header_3")
        self.header_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.header_3, 1, 0, 1, 2)

        self.fast_ema_period_input = QLineEdit(self.frame)
        self.fast_ema_period_input.setObjectName(u"fast_ema_period_input")

        self.gridLayout.addWidget(self.fast_ema_period_input, 10, 1, 1, 1)

        self.mart_coef_lbl = QLabel(self.frame)
        self.mart_coef_lbl.setObjectName(u"mart_coef_lbl")

        self.gridLayout.addWidget(self.mart_coef_lbl, 12, 0, 1, 1)

        self.leverage_lbl = QLabel(self.frame)
        self.leverage_lbl.setObjectName(u"leverage_lbl")

        self.gridLayout.addWidget(self.leverage_lbl, 4, 0, 1, 1)

        self.max_mart_depth_input = QLineEdit(self.frame)
        self.max_mart_depth_input.setObjectName(u"max_mart_depth_input")

        self.gridLayout.addWidget(self.max_mart_depth_input, 11, 1, 1, 1)

        self.min_delta_perc_lbl = QLabel(self.frame)
        self.min_delta_perc_lbl.setObjectName(u"min_delta_perc_lbl")

        self.gridLayout.addWidget(self.min_delta_perc_lbl, 14, 0, 1, 1)

        self.symbol_input = QLineEdit(self.frame)
        self.symbol_input.setObjectName(u"symbol_input")
        self.symbol_input.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.symbol_input, 2, 1, 1, 1)

        self.slow_ema_period_lbl = QLabel(self.frame)
        self.slow_ema_period_lbl.setObjectName(u"slow_ema_period_lbl")
        self.slow_ema_period_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.slow_ema_period_lbl, 9, 0, 1, 1)

        self.tf_lbl = QLabel(self.frame)
        self.tf_lbl.setObjectName(u"tf_lbl")

        self.gridLayout.addWidget(self.tf_lbl, 3, 0, 1, 1)

        self.mart_coef_input = QLineEdit(self.frame)
        self.mart_coef_input.setObjectName(u"mart_coef_input")

        self.gridLayout.addWidget(self.mart_coef_input, 12, 1, 1, 1)

        self.deal_deposit_lbl = QLabel(self.frame)
        self.deal_deposit_lbl.setObjectName(u"deal_deposit_lbl")

        self.gridLayout.addWidget(self.deal_deposit_lbl, 5, 0, 1, 1)

        self.asset_lbl = QLabel(self.frame)
        self.asset_lbl.setObjectName(u"asset_lbl")

        self.gridLayout.addWidget(self.asset_lbl, 2, 0, 1, 1)

        self.margin_type_lbl = QLabel(self.frame)
        self.margin_type_lbl.setObjectName(u"margin_type_lbl")

        self.gridLayout.addWidget(self.margin_type_lbl, 7, 0, 1, 1)

        self.pause_bars_num_lbl = QLabel(self.frame)
        self.pause_bars_num_lbl.setObjectName(u"pause_bars_num_lbl")

        self.gridLayout.addWidget(self.pause_bars_num_lbl, 13, 0, 1, 1)

        self.leverage_input = QLineEdit(self.frame)
        self.leverage_input.setObjectName(u"leverage_input")

        self.gridLayout.addWidget(self.leverage_input, 4, 1, 1, 1)

        self.margin_type_input = QComboBox(self.frame)
        self.margin_type_input.addItem("")
        self.margin_type_input.addItem("")
        self.margin_type_input.setObjectName(u"margin_type_input")

        self.gridLayout.addWidget(self.margin_type_input, 7, 1, 1, 1)

        self.fast_ema_period_lbl = QLabel(self.frame)
        self.fast_ema_period_lbl.setObjectName(u"fast_ema_period_lbl")
        self.fast_ema_period_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.fast_ema_period_lbl, 10, 0, 1, 1)

        self.direction_lbl = QLabel(self.frame)
        self.direction_lbl.setObjectName(u"direction_lbl")

        self.gridLayout.addWidget(self.direction_lbl, 8, 0, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 15, 0, 1, 1)

        self.max_deal_deposit = QLabel(self.frame)
        self.max_deal_deposit.setObjectName(u"max_deal_deposit")

        self.gridLayout.addWidget(self.max_deal_deposit, 15, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 3)

        self.gridLayout_3.addWidget(self.frame, 3, 2, 4, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.clean_input_btn = QPushButton(self.tab_settings)
        self.clean_input_btn.setObjectName(u"clean_input_btn")

        self.verticalLayout_3.addWidget(self.clean_input_btn)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 2, 1, 1)

        self.add_asset_cfg_btn = QPushButton(self.tab_settings)
        self.add_asset_cfg_btn.setObjectName(u"add_asset_cfg_btn")

        self.gridLayout_3.addWidget(self.add_asset_cfg_btn, 5, 3, 1, 1)

        self.label_5 = QLabel(self.tab_settings)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.frame1 = QFrame(self.tab_settings)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setFrameShape(QFrame.Box)
        self.gridLayout_6 = QGridLayout(self.frame1)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 1, -1, -1)
        self.account_mode_lbl = QLabel(self.frame1)
        self.account_mode_lbl.setObjectName(u"account_mode_lbl")

        self.gridLayout_6.addWidget(self.account_mode_lbl, 1, 0, 1, 1)

        self.btc_stop_short_input = QLineEdit(self.frame1)
        self.btc_stop_short_input.setObjectName(u"btc_stop_short_input")

        self.gridLayout_6.addWidget(self.btc_stop_short_input, 3, 1, 1, 1)

        self.label_3 = QLabel(self.frame1)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 3, 0, 1, 1)

        self.max_simultaneous_deals_lbl = QLabel(self.frame1)
        self.max_simultaneous_deals_lbl.setObjectName(u"max_simultaneous_deals_lbl")

        self.gridLayout_6.addWidget(self.max_simultaneous_deals_lbl, 0, 0, 1, 1)

        self.btc_stop_long_input = QLineEdit(self.frame1)
        self.btc_stop_long_input.setObjectName(u"btc_stop_long_input")

        self.gridLayout_6.addWidget(self.btc_stop_long_input, 2, 1, 1, 1)

        self.label_4 = QLabel(self.frame1)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 4, 0, 1, 1)

        self.account_mode_input = QComboBox(self.frame1)
        self.account_mode_input.addItem("")
        self.account_mode_input.addItem("")
        self.account_mode_input.setObjectName(u"account_mode_input")

        self.gridLayout_6.addWidget(self.account_mode_input, 1, 1, 1, 1)

        self.max_simultaneous_deals_input = QLineEdit(self.frame1)
        self.max_simultaneous_deals_input.setObjectName(u"max_simultaneous_deals_input")

        self.gridLayout_6.addWidget(self.max_simultaneous_deals_input, 0, 1, 1, 1)

        self.current_btc_price_lbl = QLabel(self.frame1)
        self.current_btc_price_lbl.setObjectName(u"current_btc_price_lbl")

        self.gridLayout_6.addWidget(self.current_btc_price_lbl, 4, 1, 1, 1)

        self.label_2 = QLabel(self.frame1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_6.addWidget(self.label_2, 2, 0, 1, 1)

        self.update_btc_price_btn = QPushButton(self.frame1)
        self.update_btc_price_btn.setObjectName(u"update_btc_price_btn")

        self.gridLayout_6.addWidget(self.update_btc_price_btn, 4, 2, 1, 1)

        self.apply_strat_settings_btn = QPushButton(self.frame1)
        self.apply_strat_settings_btn.setObjectName(u"apply_strat_settings_btn")

        self.gridLayout_6.addWidget(self.apply_strat_settings_btn, 0, 2, 4, 1)


        self.gridLayout_3.addWidget(self.frame1, 0, 0, 1, 1)

        self.frame2 = QFrame(self.tab_settings)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setFrameShape(QFrame.Box)
        self.gridLayout_2 = QGridLayout(self.frame2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rp_lbl = QLabel(self.frame2)
        self.rp_lbl.setObjectName(u"rp_lbl")
        self.rp_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.rp_lbl, 1, 1, 1, 1)

        self.tp1_lbl = QLabel(self.frame2)
        self.tp1_lbl.setObjectName(u"tp1_lbl")

        self.gridLayout_2.addWidget(self.tp1_lbl, 3, 0, 1, 1)

        self.ema_cross_close_lbl = QLabel(self.frame2)
        self.ema_cross_close_lbl.setObjectName(u"ema_cross_close_lbl")

        self.gridLayout_2.addWidget(self.ema_cross_close_lbl, 4, 0, 1, 1)

        self.sl_input = QLineEdit(self.frame2)
        self.sl_input.setObjectName(u"sl_input")

        self.gridLayout_2.addWidget(self.sl_input, 2, 1, 1, 1)

        self.sl_lbl = QLabel(self.frame2)
        self.sl_lbl.setObjectName(u"sl_lbl")

        self.gridLayout_2.addWidget(self.sl_lbl, 2, 0, 1, 1)

        self.ema_cross_tp_input = QLineEdit(self.frame2)
        self.ema_cross_tp_input.setObjectName(u"ema_cross_tp_input")

        self.gridLayout_2.addWidget(self.ema_cross_tp_input, 4, 1, 1, 1)

        self.tp_input = QLineEdit(self.frame2)
        self.tp_input.setObjectName(u"tp_input")

        self.gridLayout_2.addWidget(self.tp_input, 3, 1, 1, 1)

        self.header_2 = QLabel(self.frame2)
        self.header_2.setObjectName(u"header_2")
        self.header_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.header_2, 0, 0, 1, 2)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setColumnStretch(0, 1)

        self.gridLayout_3.addWidget(self.frame2, 4, 3, 1, 1)

        self.tabWidget.addTab(self.tab_settings, "")

        self.gridLayout_12.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1240, 23))
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
        self.save_cfg_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0442\u0435\u043a\u0443\u0449\u0443\u044e \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044e", None))
        self.filter_delta_limit.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0435\u043d", None))
        self.filter_slow_ema_period_input.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u041c\u0435\u0434\u043b\u0435\u043d\u043d\u043e\u0439\n"
"\u0415\u041c\u0410 (\u0431\u0430\u0440\u043e\u0432)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0444\u0440\u0435\u0439\u043c", None))
        self.filter_tf_input.setItemText(0, QCoreApplication.translate("MainWindow", u"1m", None))
        self.filter_tf_input.setItemText(1, QCoreApplication.translate("MainWindow", u"3m", None))
        self.filter_tf_input.setItemText(2, QCoreApplication.translate("MainWindow", u"5m", None))
        self.filter_tf_input.setItemText(3, QCoreApplication.translate("MainWindow", u"15m", None))
        self.filter_tf_input.setItemText(4, QCoreApplication.translate("MainWindow", u"30m", None))
        self.filter_tf_input.setItemText(5, QCoreApplication.translate("MainWindow", u"1h", None))
        self.filter_tf_input.setItemText(6, QCoreApplication.translate("MainWindow", u"4h", None))
        self.filter_tf_input.setItemText(7, QCoreApplication.translate("MainWindow", u"6h", None))
        self.filter_tf_input.setItemText(8, QCoreApplication.translate("MainWindow", u"12h", None))

        self.filter_enabled_chkbx.setText("")
        self.filter_fast_ema_period_input.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0441. \u0440\u0430\u0437\u0440\u0435\u0448 \u0434\u0435\u043b\u044c\u0442\u0430 (%)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0411\u044b\u0441\u0442\u0440\u043e\u0439\n"
"\u0415\u041c\u0410 (\u0431\u0430\u0440\u043e\u0432)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440:", None))
        self.total_symbols.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435\u0433\u043e \u043f\u0430\u0440:", None))
        self.total_symbols_val.setText("")
        self.tf_input.setItemText(0, QCoreApplication.translate("MainWindow", u"1m", None))
        self.tf_input.setItemText(1, QCoreApplication.translate("MainWindow", u"3m", None))
        self.tf_input.setItemText(2, QCoreApplication.translate("MainWindow", u"5m", None))
        self.tf_input.setItemText(3, QCoreApplication.translate("MainWindow", u"15m", None))
        self.tf_input.setItemText(4, QCoreApplication.translate("MainWindow", u"30m", None))
        self.tf_input.setItemText(5, QCoreApplication.translate("MainWindow", u"1h", None))
        self.tf_input.setItemText(6, QCoreApplication.translate("MainWindow", u"4h", None))
        self.tf_input.setItemText(7, QCoreApplication.translate("MainWindow", u"6h", None))
        self.tf_input.setItemText(8, QCoreApplication.translate("MainWindow", u"12h", None))

        self.max_mart_depth_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e\n"
"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u041e\u0440\u0434\u0435\u0440\u043e\u0432", None))
        self.deal_deposit_input.setInputMask("")
        self.slow_ema_period_input.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.pause_bars_num_input.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.allowed_direction_input.setItemText(0, QCoreApplication.translate("MainWindow", u"BOTH", None))
        self.allowed_direction_input.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u044c\u043a\u043e LONG", None))
        self.allowed_direction_input.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u044c\u043a\u043e SHORT", None))

        self.min_delta_perc_input.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.header_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0435\u043c\u0435\u0442\u0440\u044b \u0432\u0445\u043e\u0434\u0430 \u0432 \u0441\u0434\u0435\u043b\u043a\u0443:", None))
        self.fast_ema_period_input.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.mart_coef_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u0438\u0435 \u043f\u0440\u0438 \u041c\u0430\u0440\u0442\u0438\u043d\u0433\u0435\u0439\u043b, %", None))
        self.leverage_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0435\u0447\u043e", None))
        self.max_mart_depth_input.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.min_delta_perc_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d. \u0414\u0435\u043b\u044c\u0442\u0430 \u0434\u043e\u043a\u0443\u043f\u0430, %", None))
        self.slow_ema_period_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u041c\u0435\u0434\u043b\u0435\u043d\u043d\u043e\u0439\n"
"\u0415\u041c\u0410 (\u0431\u0430\u0440\u043e\u0432)", None))
        self.tf_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0444\u0440\u0435\u0439\u043c", None))
        self.mart_coef_input.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.deal_deposit_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 1 \u0412\u0445\u043e\u0434\u0430\n"
"(\u0431\u0435\u0437 \u0443\u0447\u0451\u0442\u0430 \u043f\u043b\u0435\u0447\u0430)", None))
        self.asset_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432", None))
        self.margin_type_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u041c\u0430\u0440\u0436\u0438", None))
        self.pause_bars_num_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0443\u0437\u0430, \u043a\u043e\u043b-\u0432\u043e \u0411\u0430\u0440\u043e\u0432", None))
        self.leverage_input.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.margin_type_input.setItemText(0, QCoreApplication.translate("MainWindow", u"ISOLATED", None))
        self.margin_type_input.setItemText(1, QCoreApplication.translate("MainWindow", u"CROSSED", None))

        self.fast_ema_period_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0411\u044b\u0441\u0442\u0440\u043e\u0439\n"
"\u0415\u041c\u0410 (\u0431\u0430\u0440\u043e\u0432)", None))
        self.direction_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0434\u0435\u043f\u043e\u0437\u0438\u0442<br/>\u0432 \u0441\u0434\u0435\u043b\u043a\u0435:</span></p></body></html>", None))
        self.max_deal_deposit.setText("")
        self.clean_input_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0432\u0432\u043e\u0434", None))
        self.add_asset_cfg_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u044b\u0435 \u0410\u043a\u0442\u0438\u0432\u044b", None))
        self.account_mode_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.btc_stop_short_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BTC \u0440\u0430\u0441\u0442\u0451\u0442", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043f \u0448\u043e\u0440\u0442 \u043f\u043e BTC ", None))
        self.max_simultaneous_deals_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0434\u0435\u043b\u043e\u043a \u043e\u0434\u043d\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e (\u043c\u0430\u043a\u0441 10)", None))
        self.btc_stop_long_input.setInputMask("")
        self.btc_stop_long_input.setText("")
        self.btc_stop_long_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BTC \u043f\u0430\u0434\u0430\u0435\u0442", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0446\u0435\u043d\u0430 BTC:", None))
        self.account_mode_input.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041e\u0434\u043d\u043e\u0441\u0442\u043e\u0440\u043e\u043d\u043d\u0438\u0439", None))
        self.account_mode_input.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0425\u044d\u0434\u0436", None))

        self.max_simultaneous_deals_input.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.current_btc_price_lbl.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043f \u043b\u043e\u043d\u0433 \u043f\u043e BTC ", None))
        self.update_btc_price_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.apply_strat_settings_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.rp_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (%)", None))
        self.tp1_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0422\u041f", None))
        self.ema_cross_close_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434 EMA CROSS", None))
        self.sl_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043f", None))
        self.ema_cross_tp_input.setInputMask("")
        self.ema_cross_tp_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d. % \u0434\u043b\u044f \u043e\u0442\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
        self.header_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0435\u043c\u0435\u0442\u0440\u044b \u0432\u044b\u0445\u043e\u0434\u0430 \u0438\u0437 \u0441\u0434\u0435\u043b\u043a\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
    # retranslateUi

