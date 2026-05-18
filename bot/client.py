import time
import hmac
import hashlib
import requests

BASE_URL = "https://testnet.binancefuture.com"


class BinanceFuturesClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def _sign(self, params):
        query_string = "&".join([f"{k}={v}" for k, v in params.items()])

        signature = hmac.new(
            self.api_secret.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()

        return signature

    def get_account(self):
        endpoint = "/fapi/v2/account"

        params = {
            "timestamp": int(time.time() * 1000)
        }

        query_string = "&".join([f"{k}={v}" for k, v in params.items()])

        signature = self._sign(params)

        url = f"{BASE_URL}{endpoint}?{query_string}&signature={signature}"

        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.get(url, headers=headers)

        return response.json()

    def place_market_order(self, symbol, side, quantity):
        endpoint = "/fapi/v1/order"

        params = {
            "symbol": symbol,
            "side": side.upper(),
            "type": "MARKET",
            "quantity": quantity,
            "timestamp": int(time.time() * 1000)
        }

        query_string = "&".join([f"{k}={v}" for k, v in params.items()])

        signature = self._sign(params)

        url = f"{BASE_URL}{endpoint}?{query_string}&signature={signature}"

        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url, headers=headers)

        return response.json()

    def place_limit_order(self, symbol, side, quantity, price):
        endpoint = "/fapi/v1/order"

        params = {
            "symbol": symbol,
            "side": side.upper(),
            "type": "LIMIT",
            "timeInForce": "GTC",
            "quantity": quantity,
            "price": price,
            "timestamp": int(time.time() * 1000)
        }

        query_string = "&".join([f"{k}={v}" for k, v in params.items()])

        signature = self._sign(params)

        url = f"{BASE_URL}{endpoint}?{query_string}&signature={signature}"

        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(url, headers=headers)

        return response.json()