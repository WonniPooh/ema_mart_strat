import json
import sqlite3
import time
import os
from common import *

DB_DIR = ""
RESULTS_DB = "results.db"

def get_symbols_general_info(ts_from=None, ts_till=None, db_name=RESULTS_DB):
    db_path = DB_DIR + db_name

    con = sqlite3.connect(db_path)
    req = "SELECT symbol, min(ts_start), max(ts_start), count(deal_id), SUM(case when total_result >= 0 then 1 else 0 end), SUM(case when total_result < 0 then 1 else 0 end), SUM(total_result), SUM(case when total_result >= 0 then total_result else 0 end), SUM(case when total_result < 0 then total_result else 0 end) from deals"
    if ts_from is not None or ts_till is not None:
        req += " WHERE"

        if ts_from is not None:
            req += f" ts_start >= {ts_from}"

            if ts_till is not None:
                req += " AND"

        if ts_till is not None:
            req += f" ts_end < {ts_till}"

    req += " GROUP BY symbol;"

    try:
        cur = con.cursor()
        cur.execute(req)

        data = cur.fetchall()
        return data
    except Exception as e:
        handle_exception(e)
    finally:
        con.close()

def get_config(config_id, db_name=RESULTS_DB):
    db_path = DB_DIR + db_name

    con = sqlite3.connect(db_path)
    req = f"SELECT * from configs where record_id = {config_id};"

    try:
        cur = con.cursor()
        cur.execute(req)

        data = cur.fetchall()
        return data[0]
    except Exception as e:
        handle_exception(e)
    finally:
        con.close()

def get_symbol_deals_stat(symbol, ts_start=None, ts_end=None, db_name=RESULTS_DB):
    db_path = DB_DIR + db_name

    con = sqlite3.connect(db_path)
    cond = ""
    if symbol != "ALL":
        cond = f"WHERE symbol=\'{symbol}\'"

    if ts_start is not None:
        if len(cond) > 0:
            cond += " AND"
        else:
            cond += " WHERE"
        cond += f" ts_start >= {ts_start}"

    if ts_end is not None:
        if len(cond) > 0:
            cond += " AND"
        else:
            cond += " WHERE"
        cond += f" ts_end < {ts_end}"

    req_positive = f"SELECT count(deal_id), SUM(total_result), SUM(total_result/total_position) from deals {cond} AND total_result >= 0;"
    req_negative = f"SELECT count(deal_id), SUM(total_result), SUM(total_result/total_position) from deals {cond} AND total_result < 0;"
    req_total = f"SELECT count(deal_id), SUM(total_result), SUM(total_result/total_position) from deals {cond};"

    try:
        cur = con.cursor()
        cur.execute(req_positive)
        data_positive = cur.fetchall()
        if data_positive[0][1] is None:
            data_positive = [[0,0,0]]
        
        cur.execute(req_negative)
        data_negative = cur.fetchall()
        if data_negative[0][1] is None:
            data_negative = [[0,0,0]]

        cur.execute(req_total)
        data_total = cur.fetchall()
        if data_total[0][1] is None:
            data_total = [[0,0,0]]

        return [data_positive, data_negative, data_total]
    except Exception as e:
        handle_exception(e)
    finally:
        con.close()


def get_symbol_deals(symbol, ts_start=None, ts_end=None, db_name=RESULTS_DB):
    db_path = DB_DIR + db_name

    con = sqlite3.connect(db_path)
    cond = ""
    if symbol != "ALL":
        cond = f"WHERE symbol=\'{symbol}\'"

    if ts_start is not None:
        if len(cond) > 0:
            cond += " AND"
        else:
            cond += " WHERE"
        cond += f" ts_start >= {ts_start}"

    if ts_end is not None:
        if len(cond) > 0:
            cond += " AND"
        else:
            cond += " WHERE"
        cond += f" ts_end <= {ts_end}"

    req = f"SELECT config_id, symbol, side, total_position, mart_steps, \
                    total_commission, total_result, total_result/total_position, \
                    ts_start, ts_end from deals {cond} ;"
    try:
        cur = con.cursor()
        cur.execute(req)

        data = cur.fetchall()
        data_as_list = []
        for elem in data:
            try:
                data_as_list.append(list(elem))
                data_as_list[-1][2] = "LONG" if data_as_list[-1][2] == 1 else "SHORT"
                data_as_list[-1][-1] = datetime.fromtimestamp(data_as_list[-1][-1]).strftime("%d.%m %H:%M:%S")
                data_as_list[-1][-2] = datetime.fromtimestamp(data_as_list[-1][-2]).strftime("%d.%m %H:%M:%S")
                data_as_list[-1][-3] = float(round(data_as_list[-1][-3], 2)) 
            except Exception as e:
                handle_exception(e)
                continue
        return data_as_list
    except Exception as e:
        handle_exception(e)
    finally:
        con.close()

def get_deal_orders(deal_id, db_name=RESULTS_DB):
    db_path = DB_DIR + db_name
    con = sqlite3.connect(db_path)
    req = f"SELECT symbol, type, side, base_amount, price, base_amount*price, commission, ts_filled from orders WHERE deal_id={deal_id};"

    try:
        cur = con.cursor()
        cur.execute(req)

        data = cur.fetchall()
        data_as_list = []
        for elem in data:
            try:
                data_as_list.append(list(elem))
                data_as_list[-1][2] = "LONG" if data_as_list[-1][2] == 1 else "SHORT"
                data_as_list[-1][5] = round(float(data_as_list[-1][5]), 2)
                data_as_list[-1][-1] = datetime.fromtimestamp(data_as_list[-1][-1]).strftime("%d.%m %H:%M:%S")
            except Exception as e:
                handle_exception(e)
                continue
        return data_as_list
    except Exception as e:
        handle_exception(e)
    finally:
        con.close()

