import time
import requests
import json
import hmac
from common import handle_exception
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
FUTURES_CONTRACTS_URL = "/openApi/swap/v2/quote/contracts"
FUTURES_PRICES_URL = "/openApi/swap/v1/ticker/price"
FUTURES_KLINES_URL = "/openApi/swap/v3/quote/klines"
FUTURES_SET_LEVERAGE_URL = "/openApi/swap/v2/trade/leverage"

APIKEY = ""
SECRETKEY = ""

with open("account.json") as f:
    keys = f.read()
    keys = keys.split("\n")
    APIKEY = keys[0]
    SECRETKEY = keys[1]

def retry_handle_except(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                handle_exception(e)
                if i < 3:
                    time.sleep(0.5)
                else:
                    return None
    
    return wrapper

@retry_handle_except
def get_available_futures_contracts():
    method = "GET"
    path = FUTURES_CONTRACTS_URL
    result = send_request(method, path)
    jsoned_result = json.loads(result)
    if jsoned_result["code"] != 0:
        print(f"Error appeared during 'get_current_price': {jsoned_result}")

    data = jsoned_result.get("data")
    parsed = {}
    for pair_data in data:
        if pair_data["maxLongLeverage"] != pair_data["maxShortLeverage"]:
            print(f"Skip symbol {pair_data['symbol']} due to Long MAxLeverage != Short MaxLeverage")
            continue

        parsed[pair_data["symbol"]] = pair_data

    return parsed
        
@retry_handle_except
def get_current_price(symbol=None):
    method = "GET"
    path = FUTURES_PRICES_URL
    params = {}
    if symbol is not None:
        params = {"symbol": symbol}
    result = send_request(method, path, params)
    jsoned_result = json.loads(result)
    if jsoned_result["code"] != 0:
        print(f"Error appeared during 'get_current_price': {jsoned_result}")

    parsed = {}
    for pair_data in jsoned_result["data"]:
        parsed[pair_data["symbol"]] = float(pair_data["price"])

    return parsed

@retry_handle_except
def get_open_orders(symbol=None):
    path = '/openApi/swap/v2/trade/openOrders'
    method = "GET"
    paramsMap = {}
    if symbol is not None:
        paramsMap["symbol"] = symbol.upper()

    result = send_request(method, path, paramsMap)
    jsoned_result = json.loads(result)
    if jsoned_result["code"] != 0:
        print(f"Error appeared during 'get_open_orders': {jsoned_result}")

    return jsoned_result

@retry_handle_except
def get_account_uid(symbol=None):
    path = '/openApi/account/v1/uid'
    method = "GET"
    paramsMap = {}
    result = send_request(method, path, paramsMap)
    jsoned_result = json.loads(result)
    if jsoned_result["code"] != 0:
        print(f"Error appeared during 'get_account_uid': {jsoned_result}")

    return jsoned_result

@retry_handle_except
def load_klines(symbol, timeframe, ts_start_ms=None):
    path = FUTURES_KLINES_URL
    method = "GET"
    paramsMap = {
        "symbol": symbol.upper(),
        "interval": timeframe,
        "limit": "1000",
    }

    if ts_start_ms is not None:
        parseParam["startTime"] = str(ts_start_ms)

    result = send_request(method, path, paramsMap)
    jsoned_result = json.loads(result)

    if jsoned_result["code"] != 0:
        print(f"Error appeared during 'load_klines': {jsoned_result}")
        return None

    data = jsoned_result["data"]
    data.reverse()
    return data

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    return signature

@retry_handle_except
def send_request(method, path, urlpa={}, payload={}):
    urlpa = parseParam(urlpa)
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlpa, get_sign(SECRETKEY, urlpa))
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

@retry_handle_except
def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsStr = "&".join(["%s=%s" % (x, paramsMap[x]) for x in sortedKeys])
    if paramsStr != "":
     return paramsStr+"&timestamp="+str(int(time.time() * 1000))
    else:
     return paramsStr+"timestamp="+str(int(time.time() * 1000))

@retry_handle_except
def get_balance(): #availableMargin, balance
    path = '/openApi/swap/v2/user/balance'
    method = "GET"

    result = send_request(method, path)
    jsoned_result = json.loads(result)
    if jsoned_result["code"] != 0:
       print(f"Error appeared during 'get_balance': {jsoned_result}")

    return jsoned_result["data"]["balance"]

@retry_handle_except
def set_leverage(leverage, symbol, is_single_side=True):
    path = FUTURES_SET_LEVERAGE_URL
    method = "POST"
    paramsMap = {
        "leverage": str(int(leverage)),
        "symbol": symbol.upper()
    }
    arr = ["LONG", "SHORT"]
    if is_single_side:
        arr = ["BOTH"]

    for side in arr:
        paramsMap['side'] = side
        result = send_request(method, path, paramsMap)
        jsoned_result = json.loads(result)
        print(jsoned_result)
        if jsoned_result["code"] != 0:
            print(f"Error appeared during 'set_leverage' {side} change: {jsoned_result}")

@retry_handle_except
def change_dual_side(is_dual_side: bool):
    path = '/openApi/swap/v1/positionSide/dual'
    method = "POST"
    paramsMap = {
        "dualSidePosition": str(is_dual_side).lower()
    }

    result = send_request(method, path, paramsMap)
    jsoned_result = json.loads(result)
    if jsoned_result["code"] != 0:
       print(f"Error appeared during 'change_dual_side': {jsoned_result}")
    else:
        print(f"Dual side position change success: {jsoned_result}")

@retry_handle_except
def get_order_details(symbol, order_id):
   path = '/openApi/swap/v2/trade/order'
   method = "GET"
   paramsMap = {
       "orderId": order_id,
       "symbol": symbol.upper()
   }
   result = send_request(method, path, paramsMap)
   jsoned_result = json.loads(result)
   if jsoned_result["code"] != 0:
      print(f"Error appeared during 'get_order_details': {jsoned_result}")

   return jsoned_result

@retry_handle_except
def new_market_order(symbol, side, quantity):
   path = '/openApi/swap/v2/trade/order'
   method = "POST"
   paramsMap = {
       "symbol": symbol.upper(),
       "side": side.upper(),
       "positionSide": "BOTH",
       "type": "MARKET",
       "quantity": quantity #coins amount
   }

   result = send_request(method, path, paramsMap)
   jsoned_result = json.loads(result)
   if jsoned_result["code"] != 0:
      print(f"Error appeared during 'new_market_order': {jsoned_result}")

   return jsoned_result

#def new_limit_order(symbol, side, quantity, price):
#   path = '/openApi/swap/v2/trade/order'
#   method = "POST"
#   paramsMap = {
#       "symbol": symbol.upper(),
#       "side": side.upper(),
#       "positionSide": "BOTH",
#       "type": "MARKET",
#       "quantity": quantity, #coins amount
#       "price": price
#   }

#def cancel_all_orders(symbol=None):
#   path = '/openApi/swap/v2/trade/allOpenOrders'
#   method = "DELETE"
#   paramsMap = {
#       "recvWindow": "0"
#   }

#   if symbol is not None:
#       paramsMap["symbol"] = symbol.upper()
