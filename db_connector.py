import sqlite3
import time
import json
from common import *

db_path = "results.db"
#TODO add accounts handling code

def construct_db():
    try:
        con = sqlite3.connect(db_path)
        try:
            cur = con.cursor()

            create_deals_table = '''CREATE TABLE IF NOT EXISTS deals
                                   (deal_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    symbol STRING NOT NULL,
                                    config_id INTEGER NOT NULL,
                                    side BOOL NOT NULL,              
                                    ts_start INTEGER NOT NULL,
                                    ts_end INTEGER,
                                    total_result FLOAT,
                                    FOREIGN KEY(config_id) REFERENCES configs(record_id));'''
            cur.execute(create_deals_table)
            con.commit()

            create_orders_table = '''CREATE TABLE IF NOT EXISTS orders
                                   (order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    exchange_order_id INTEGER NOT NULL,
                                    deal_id INTEGER NOT NULL,
                                    symbol STRING NOT NULL,
                                    side BOOL NOT NULL,
                                    type STRING NOT NULL,
                                    ts_filled INTEGER NOT NULL,
                                    price FLOAT NOT NULL,
                                    base_amount FLOAT,
                                    commission FLOAT,
                                    FOREIGN KEY(deal_id) REFERENCES deals(deal_id));'''
            cur.execute(create_orders_table)
            con.commit()

            create_configs_table = '''CREATE TABLE IF NOT EXISTS configs
                                      (record_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                       config STRING NOT NULL);'''
            cur.execute(create_configs_table)
            con.commit()

            create_balance_table = '''CREATE TABLE IF NOT EXISTS balance
                                       (record_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        timestamp INTEGER NOT NULL,
                                        balance FLOAT NOT NULL)'''
            cur.execute(create_balance_table)
            con.commit()

        finally:
            con.close()

    except Exception as e:
        handle_exception(e)

def db_insert_config(cfg):
    con = sqlite3.connect(db_path)
    req = f"SELECT record_id from configs WHERE config=\'{cfg}\';"
    set_cfg = f'''INSERT INTO configs VALUES (NULL, \'{cfg}\')'''

    try:
        cur = con.cursor()

        cur.execute(req)
        data = cur.fetchall()
        if len(data) > 0:
            return data[0][0]

        cur.execute(set_cfg)
        con.commit()
        return cur.lastrowid
    except Exception as e:
        handle_exception(e)
    finally:
        con.close()

def db_update_balance(balance):
    con = sqlite3.connect(db_path)
    timestamp = int(time.time())
    set_balance = f'''INSERT INTO balance VALUES (NULL, {timestamp}, {balance})'''
    try:
        cur = con.cursor()
        cur.execute(set_balance)
        con.commit()
    except Exception as e:
        handle_exception(e)
    finally:
        con.close()


def db_new_deal(deal):
    con = sqlite3.connect(db_path)

    #deal_open_cmd contains actual values (absolute) of TP and SL
    set_finished_deal = f'''INSERT INTO deals VALUES (NULL, \"{deal.symbol}\",
                                                        {deal.config_id},
                                                        {deal.current_position_side},
                                                        {deal.ts_deal_start},
                                                        NULL, NULL)'''


    try:
        cur = con.cursor()
        cur.execute(set_finished_deal)
        con.commit()
        return cur.lastrowid
    except Exception as e:
        handle_exception(e)
    finally:
        con.close()

def db_new_finished_deal(deal_id, finished_deal):
    con = sqlite3.connect(db_path)

    #deal_open_cmd contains actual values (absolute) of TP and SL
    set_finished_deal = f'''UPDATE deals SET ts_end={finished_deal.timestamp_end},
                                             total_result={finished_deal.total_result}
                                         WHERE deal_id={deal_id}'''

    try:
        cur = con.cursor()
        cur.execute(set_finished_deal)
        con.commit()
    except Exception as e:
        handle_exception(e)
    finally:
        con.close()


def db_new_finished_order(finished_order, deal_id):
    con = sqlite3.connect(db_path)

    set_finished_order = f'''INSERT INTO orders VALUES (NULL, \"{finished_order["data"]["order"]["orderId"]}\",
                                                        {deal_id},
                                                        \"{finished_order["data"]["order"]["symbol"]}\",
                                                        {finished_order["data"]["order"]["side"]=="BUY"},
                                                        \"{finished_order["data"]["order"]["type"]}\",
                                                        {int(time.time())},
                                                        {finished_order["data"]["order"]["avgPrice"]},
                                                        {float(finished_order["data"]["order"]["executedQty"])},
                                                        {round(abs(float(finished_order["data"]["order"]["commission"])), 2)})'''

    try:
        cur = con.cursor()
        cur.execute(set_finished_order)
        con.commit()
    except Exception as e:
        handle_exception(e)
    finally:
        con.close()

