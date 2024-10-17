# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_report.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(798, 514)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.close_window_btn = QPushButton(Dialog)
        self.close_window_btn.setObjectName(u"close_window_btn")

        self.gridLayout.addWidget(self.close_window_btn, 4, 0, 1, 4)

        self.frame2 = QFrame(Dialog)
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
        self.sl_input.setReadOnly(True)

        self.gridLayout_2.addWidget(self.sl_input, 2, 1, 1, 1)

        self.sl_lbl = QLabel(self.frame2)
        self.sl_lbl.setObjectName(u"sl_lbl")

        self.gridLayout_2.addWidget(self.sl_lbl, 2, 0, 1, 1)

        self.ema_cross_tp_input = QLineEdit(self.frame2)
        self.ema_cross_tp_input.setObjectName(u"ema_cross_tp_input")
        self.ema_cross_tp_input.setReadOnly(True)

        self.gridLayout_2.addWidget(self.ema_cross_tp_input, 4, 1, 1, 1)

        self.tp_input = QLineEdit(self.frame2)
        self.tp_input.setObjectName(u"tp_input")
        self.tp_input.setReadOnly(True)

        self.gridLayout_2.addWidget(self.tp_input, 3, 1, 1, 1)

        self.header_2 = QLabel(self.frame2)
        self.header_2.setObjectName(u"header_2")
        self.header_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.header_2, 0, 0, 1, 2)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setColumnStretch(0, 1)

        self.gridLayout.addWidget(self.frame2, 1, 3, 1, 1)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.gridLayout1 = QGridLayout(self.frame)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.leverage_input = QLineEdit(self.frame)
        self.leverage_input.setObjectName(u"leverage_input")
        self.leverage_input.setReadOnly(True)

        self.gridLayout1.addWidget(self.leverage_input, 3, 1, 1, 1)

        self.deal_deposit_lbl = QLabel(self.frame)
        self.deal_deposit_lbl.setObjectName(u"deal_deposit_lbl")

        self.gridLayout1.addWidget(self.deal_deposit_lbl, 4, 0, 1, 1)

        self.deal_deposit_input = QLineEdit(self.frame)
        self.deal_deposit_input.setObjectName(u"deal_deposit_input")
        self.deal_deposit_input.setReadOnly(True)

        self.gridLayout1.addWidget(self.deal_deposit_input, 4, 1, 1, 1)

        self.min_delta_perc_lbl = QLabel(self.frame)
        self.min_delta_perc_lbl.setObjectName(u"min_delta_perc_lbl")

        self.gridLayout1.addWidget(self.min_delta_perc_lbl, 13, 0, 1, 1)

        self.margin_type_input = QComboBox(self.frame)
        self.margin_type_input.addItem("")
        self.margin_type_input.addItem("")
        self.margin_type_input.setObjectName(u"margin_type_input")

        self.gridLayout1.addWidget(self.margin_type_input, 6, 1, 1, 1)

        self.slow_ema_period_input = QLineEdit(self.frame)
        self.slow_ema_period_input.setObjectName(u"slow_ema_period_input")
        self.slow_ema_period_input.setReadOnly(True)

        self.gridLayout1.addWidget(self.slow_ema_period_input, 8, 1, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout1.addWidget(self.label_12, 14, 0, 1, 1)

        self.pause_bars_num_lbl = QLabel(self.frame)
        self.pause_bars_num_lbl.setObjectName(u"pause_bars_num_lbl")

        self.gridLayout1.addWidget(self.pause_bars_num_lbl, 12, 0, 1, 1)

        self.fast_ema_period_lbl = QLabel(self.frame)
        self.fast_ema_period_lbl.setObjectName(u"fast_ema_period_lbl")
        self.fast_ema_period_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout1.addWidget(self.fast_ema_period_lbl, 9, 0, 1, 1)

        self.max_deal_deposit = QLabel(self.frame)
        self.max_deal_deposit.setObjectName(u"max_deal_deposit")

        self.gridLayout1.addWidget(self.max_deal_deposit, 14, 1, 1, 1)

        self.header_3 = QLabel(self.frame)
        self.header_3.setObjectName(u"header_3")
        self.header_3.setAlignment(Qt.AlignCenter)

        self.gridLayout1.addWidget(self.header_3, 1, 0, 1, 2)

        self.pause_bars_num_input = QLineEdit(self.frame)
        self.pause_bars_num_input.setObjectName(u"pause_bars_num_input")
        self.pause_bars_num_input.setReadOnly(True)

        self.gridLayout1.addWidget(self.pause_bars_num_input, 12, 1, 1, 1)

        self.slow_ema_period_lbl = QLabel(self.frame)
        self.slow_ema_period_lbl.setObjectName(u"slow_ema_period_lbl")
        self.slow_ema_period_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout1.addWidget(self.slow_ema_period_lbl, 8, 0, 1, 1)

        self.fast_ema_period_input = QLineEdit(self.frame)
        self.fast_ema_period_input.setObjectName(u"fast_ema_period_input")
        self.fast_ema_period_input.setReadOnly(True)

        self.gridLayout1.addWidget(self.fast_ema_period_input, 9, 1, 1, 1)

        self.leverage_lbl = QLabel(self.frame)
        self.leverage_lbl.setObjectName(u"leverage_lbl")

        self.gridLayout1.addWidget(self.leverage_lbl, 3, 0, 1, 1)

        self.direction_lbl = QLabel(self.frame)
        self.direction_lbl.setObjectName(u"direction_lbl")

        self.gridLayout1.addWidget(self.direction_lbl, 7, 0, 1, 1)

        self.max_mart_depth_input = QLineEdit(self.frame)
        self.max_mart_depth_input.setObjectName(u"max_mart_depth_input")
        self.max_mart_depth_input.setReadOnly(True)

        self.gridLayout1.addWidget(self.max_mart_depth_input, 10, 1, 1, 1)

        self.tf_lbl = QLabel(self.frame)
        self.tf_lbl.setObjectName(u"tf_lbl")

        self.gridLayout1.addWidget(self.tf_lbl, 2, 0, 1, 1)

        self.allowed_direction_input = QComboBox(self.frame)
        self.allowed_direction_input.addItem("")
        self.allowed_direction_input.addItem("")
        self.allowed_direction_input.addItem("")
        self.allowed_direction_input.setObjectName(u"allowed_direction_input")

        self.gridLayout1.addWidget(self.allowed_direction_input, 7, 1, 1, 1)

        self.mart_coef_input = QLineEdit(self.frame)
        self.mart_coef_input.setObjectName(u"mart_coef_input")
        self.mart_coef_input.setReadOnly(True)

        self.gridLayout1.addWidget(self.mart_coef_input, 11, 1, 1, 1)

        self.mart_coef_lbl = QLabel(self.frame)
        self.mart_coef_lbl.setObjectName(u"mart_coef_lbl")

        self.gridLayout1.addWidget(self.mart_coef_lbl, 11, 0, 1, 1)

        self.margin_type_lbl = QLabel(self.frame)
        self.margin_type_lbl.setObjectName(u"margin_type_lbl")

        self.gridLayout1.addWidget(self.margin_type_lbl, 6, 0, 1, 1)

        self.max_mart_depth_lbl = QLabel(self.frame)
        self.max_mart_depth_lbl.setObjectName(u"max_mart_depth_lbl")
        self.max_mart_depth_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout1.addWidget(self.max_mart_depth_lbl, 10, 0, 1, 1)

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
        self.tf_input.setEditable(False)

        self.gridLayout1.addWidget(self.tf_input, 2, 1, 1, 1)

        self.min_delta_perc_input = QLineEdit(self.frame)
        self.min_delta_perc_input.setObjectName(u"min_delta_perc_input")
        self.min_delta_perc_input.setReadOnly(True)

        self.gridLayout1.addWidget(self.min_delta_perc_input, 13, 1, 1, 1)

        self.gridLayout1.setColumnStretch(0, 3)

        self.gridLayout.addWidget(self.frame, 0, 2, 2, 1)

        self.gridFrame = QFrame(Dialog)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setFrameShape(QFrame.Box)
        self.gridLayout_7 = QGridLayout(self.gridFrame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_11 = QLabel(self.gridFrame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_7.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_9 = QLabel(self.gridFrame)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_7.addWidget(self.label_9, 6, 0, 1, 1)

        self.label_10 = QLabel(self.gridFrame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_7.addWidget(self.label_10, 7, 0, 1, 1)

        self.label_13 = QLabel(self.gridFrame)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_7.addWidget(self.label_13, 2, 0, 1, 1)

        self.filter_delta_limit = QLineEdit(self.gridFrame)
        self.filter_delta_limit.setObjectName(u"filter_delta_limit")

        self.gridLayout_7.addWidget(self.filter_delta_limit, 7, 1, 1, 1)

        self.filter_enabled_chkbx = QCheckBox(self.gridFrame)
        self.filter_enabled_chkbx.setObjectName(u"filter_enabled_chkbx")
        self.filter_enabled_chkbx.setLayoutDirection(Qt.LeftToRight)
        self.filter_enabled_chkbx.setStyleSheet(u"margin-left:50%; margin-right:50%;")

        self.gridLayout_7.addWidget(self.filter_enabled_chkbx, 1, 1, 1, 1)

        self.filter_fast_ema_period_input = QLineEdit(self.gridFrame)
        self.filter_fast_ema_period_input.setObjectName(u"filter_fast_ema_period_input")

        self.gridLayout_7.addWidget(self.filter_fast_ema_period_input, 6, 1, 1, 1)

        self.label_8 = QLabel(self.gridFrame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_7.addWidget(self.label_8, 5, 0, 1, 1)

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

        self.gridLayout_7.addWidget(self.filter_tf_input, 4, 1, 1, 1)

        self.label_7 = QLabel(self.gridFrame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_7.addWidget(self.label_7, 4, 0, 1, 1)

        self.filter_disable_position_add_chkbx = QCheckBox(self.gridFrame)
        self.filter_disable_position_add_chkbx.setObjectName(u"filter_disable_position_add_chkbx")
        self.filter_disable_position_add_chkbx.setStyleSheet(u"margin-left:50%; margin-right:50%;")

        self.gridLayout_7.addWidget(self.filter_disable_position_add_chkbx, 2, 1, 1, 1)

        self.filter_slow_ema_period_input = QLineEdit(self.gridFrame)
        self.filter_slow_ema_period_input.setObjectName(u"filter_slow_ema_period_input")

        self.gridLayout_7.addWidget(self.filter_slow_ema_period_input, 5, 1, 1, 1)

        self.label_6 = QLabel(self.gridFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 2)

        self.gridLayout_7.setRowStretch(0, 1)
        self.gridLayout_7.setColumnStretch(0, 2)

        self.gridLayout.addWidget(self.gridFrame, 0, 3, 1, 1)

        self.gridLayout.setRowStretch(0, 1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.close_window_btn.setText(QCoreApplication.translate("Dialog", u"Close", None))
        self.rp_lbl.setText(QCoreApplication.translate("Dialog", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (%)", None))
        self.tp1_lbl.setText(QCoreApplication.translate("Dialog", u"\u0422\u041f", None))
        self.ema_cross_close_lbl.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0445\u043e\u0434 EMA CROSS", None))
        self.sl_lbl.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u043e\u043f", None))
        self.ema_cross_tp_input.setInputMask("")
        self.ema_cross_tp_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041c\u0438\u043d. % \u0434\u043b\u044f \u043e\u0442\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
        self.header_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u0435\u043c\u0435\u0442\u0440\u044b \u0432\u044b\u0445\u043e\u0434\u0430 \u0438\u0437 \u0441\u0434\u0435\u043b\u043a\u0438", None))
        self.leverage_input.setText("")
        self.deal_deposit_lbl.setText(QCoreApplication.translate("Dialog", u"\u0421\u0443\u043c\u043c\u0430 1 \u0412\u0445\u043e\u0434\u0430(\u0431\u0435\u0437 \u0443\u0447\u0451\u0442\u0430 \u043f\u043b\u0435\u0447\u0430)", None))
        self.deal_deposit_input.setInputMask("")
        self.min_delta_perc_lbl.setText(QCoreApplication.translate("Dialog", u"\u041c\u0438\u043d. \u0414\u0435\u043b\u044c\u0442\u0430 \u0434\u043e\u043a\u0443\u043f\u0430, %", None))
        self.margin_type_input.setItemText(0, QCoreApplication.translate("Dialog", u"ISOLATED", None))
        self.margin_type_input.setItemText(1, QCoreApplication.translate("Dialog", u"CROSSED", None))

        self.slow_ema_period_input.setText("")
        self.label_12.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:700;\">\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0434\u0435\u043f\u043e\u0437\u0438\u0442<br/>\u0432 \u0441\u0434\u0435\u043b\u043a\u0435:</span></p></body></html>", None))
        self.pause_bars_num_lbl.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0443\u0437\u0430, \u043a\u043e\u043b-\u0432\u043e \u0411\u0430\u0440\u043e\u0432", None))
        self.fast_ema_period_lbl.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0411\u044b\u0441\u0442\u0440\u043e\u0439\u0415\u041c\u0410 (\u0431\u0430\u0440\u043e\u0432)", None))
        self.max_deal_deposit.setText("")
        self.header_3.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u0435\u043c\u0435\u0442\u0440\u044b \u0432\u0445\u043e\u0434\u0430 \u0432 \u0441\u0434\u0435\u043b\u043a\u0443:", None))
        self.pause_bars_num_input.setText("")
        self.slow_ema_period_lbl.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u041c\u0435\u0434\u043b\u0435\u043d\u043d\u043e\u0439 \u0415\u041c\u0410 (\u0431\u0430\u0440\u043e\u0432)", None))
        self.fast_ema_period_input.setText("")
        self.leverage_lbl.setText(QCoreApplication.translate("Dialog", u"\u041f\u043b\u0435\u0447\u043e", None))
        self.direction_lbl.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.max_mart_depth_input.setText("")
        self.tf_lbl.setText(QCoreApplication.translate("Dialog", u"\u0422\u0430\u0439\u043c\u0444\u0440\u0435\u0439\u043c", None))
        self.allowed_direction_input.setItemText(0, QCoreApplication.translate("Dialog", u"BOTH", None))
        self.allowed_direction_input.setItemText(1, QCoreApplication.translate("Dialog", u"\u0422\u043e\u043b\u044c\u043a\u043e LONG", None))
        self.allowed_direction_input.setItemText(2, QCoreApplication.translate("Dialog", u"\u0422\u043e\u043b\u044c\u043a\u043e SHORT", None))

        self.mart_coef_input.setText("")
        self.mart_coef_lbl.setText(QCoreApplication.translate("Dialog", u"\u0423\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u0438\u0435 \u043f\u0440\u0438 \u041c\u0430\u0440\u0442\u0438\u043d\u0433\u0435\u0439\u043b, %", None))
        self.margin_type_lbl.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f \u041c\u0430\u0440\u0436\u0438", None))
        self.max_mart_depth_lbl.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b-\u0432\u043e \u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u041e\u0440\u0434\u0435\u0440\u043e\u0432", None))
        self.tf_input.setItemText(0, QCoreApplication.translate("Dialog", u"1m", None))
        self.tf_input.setItemText(1, QCoreApplication.translate("Dialog", u"3m", None))
        self.tf_input.setItemText(2, QCoreApplication.translate("Dialog", u"5m", None))
        self.tf_input.setItemText(3, QCoreApplication.translate("Dialog", u"15m", None))
        self.tf_input.setItemText(4, QCoreApplication.translate("Dialog", u"30m", None))
        self.tf_input.setItemText(5, QCoreApplication.translate("Dialog", u"1h", None))
        self.tf_input.setItemText(6, QCoreApplication.translate("Dialog", u"4h", None))
        self.tf_input.setItemText(7, QCoreApplication.translate("Dialog", u"6h", None))
        self.tf_input.setItemText(8, QCoreApplication.translate("Dialog", u"12h", None))

        self.min_delta_perc_input.setText("")
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u0412\u043a\u043b\u044e\u0447\u0435\u043d", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0411\u044b\u0441\u0442\u0440\u043e\u0439\u0415\u041c\u0410 (\u0431\u0430\u0440\u043e\u0432)", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u041c\u0430\u043a\u0441. \u0440\u0430\u0437\u0440\u0435\u0448 \u0434\u0435\u043b\u044c\u0442\u0430 (%)", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u0442 \u0414\u043e\u043a\u0443\u043f\u043a\u0438 \u0432 \u043f\u043e\u0437\u0438\u0446\u0438\u0438", None))
        self.filter_delta_limit.setText("")
        self.filter_enabled_chkbx.setText("")
        self.filter_fast_ema_period_input.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u041c\u0435\u0434\u043b\u0435\u043d\u043d\u043e\u0439\u0415\u041c\u0410 (\u0431\u0430\u0440\u043e\u0432)", None))
        self.filter_tf_input.setItemText(0, QCoreApplication.translate("Dialog", u"1m", None))
        self.filter_tf_input.setItemText(1, QCoreApplication.translate("Dialog", u"3m", None))
        self.filter_tf_input.setItemText(2, QCoreApplication.translate("Dialog", u"5m", None))
        self.filter_tf_input.setItemText(3, QCoreApplication.translate("Dialog", u"15m", None))
        self.filter_tf_input.setItemText(4, QCoreApplication.translate("Dialog", u"30m", None))
        self.filter_tf_input.setItemText(5, QCoreApplication.translate("Dialog", u"1h", None))
        self.filter_tf_input.setItemText(6, QCoreApplication.translate("Dialog", u"4h", None))
        self.filter_tf_input.setItemText(7, QCoreApplication.translate("Dialog", u"6h", None))
        self.filter_tf_input.setItemText(8, QCoreApplication.translate("Dialog", u"12h", None))

        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0422\u0430\u0439\u043c\u0444\u0440\u0435\u0439\u043c", None))
        self.filter_disable_position_add_chkbx.setText("")
        self.filter_slow_ema_period_input.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0424\u0438\u043b\u044c\u0442\u0440:", None))
    # retranslateUi

