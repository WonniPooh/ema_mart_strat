# This Python file uses the following encoding: utf-8
import sys, os
import importlib.util
import queue

def handle_exception(fired_exception, comment=""):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    log_message = f"{fname}:{exc_tb.tb_lineno} - {exc_type}:{fired_exception}"
    if len(comment) > 0:
        log_message += f"\nComment:{comment}"
    print(log_message)

MSG_QUEUE = queue.Queue()
def log_msg(msg):
    MSG_QUEUE.put_nowait(msg)


KLINES_INTERVAL_DURATION = {"1m": 60, "3m": 180, "5m": 300, "15m": 900, "30m": 1800, "1h": 3600, "2h": 7200,
                               "4h": 14400, "6h": 21600, "8h": 28800, "12h": 43200, "1d": 86400, "3d": 259200,
                               "1w": 604800}

DEBUG = True
