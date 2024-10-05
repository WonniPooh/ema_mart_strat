# This Python file uses the following encoding: utf-8
import json
import time
from datetime import datetime

from PySide6 import QtCore, QtWebSockets, QtNetwork

#TODO no close frame received or sent
class WsConnector:
    def __init__(self, msg_processor, on_connect=None):
        self.client = QtWebSockets.QWebSocket("", QtWebSockets.QWebSocketProtocol.Version13, None)
        self.client.error.connect(self.onError)
        self.client.connected.connect(self.onConnected)
        self.client.textMessageReceived.connect(self.onNewMessage)

        self.restart_timer = QtCore.QTimer()
        self.restart_timer.setSingleShot(True)
        self.restart_timer.timeout.connect(self.try_connect)
        self.reconnect_ms_interval = 5000
        self.on_connect = on_connect

        self.process_income_msg = msg_processor
        self.try_connect()

    def onNewMessage(self, msg):
        print(f"{datetime.now()} client: recv_message: ", msg)
        self.process_income_msg(msg)

    def onConnected(self):
        self.send_message("secret_password")
        if self.on_connect is not None:
            self.on_connect()
            self.on_connect = None

    # def do_ping(self):
    #     print("client: do_ping")
    #     self.send_message(json.dumps({"username":f"{ACC_USERNAME}", "cmd":"PING"}))

    def send_message(self, message):
        print(f"{datetime.now()} client: send_message: ", message)
        if self.client.isValid():
            self.client.sendTextMessage(message)
        else:
            print(f"WS connection is DOWN, can't send msg:\n{message}")
            self.client.close()
            self.restart_timer.start(self.reconnect_ms_interval)

    def try_connect(self):
        print("trying to connect...")
        self.client.open(QtCore.QUrl("ws://127.0.0.1:8877"))

    def onError(self, error_code):
        print("WS FAILED: error code: {}".format(error_code))
        print(self.client.errorString())

        try:
            self.client.close()
        except Exception as e:
            print(e)

        self.restart_timer.start(self.reconnect_ms_interval)

    def onDisconnect(self):
        try:
            self.client.close()
        except Exception as e:
            print(e)

        self.restart_timer.start(self.reconnect_ms_interval)

    def close(self):
        self.client.close()

