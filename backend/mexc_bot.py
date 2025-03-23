import requests
import hashlib
import hmac
import time
from config import Config

class MEXCTradingBot:
    def __init__(self):
        self.api_key = Config.MEXC_API_KEY
        self.secret_key = Config.MEXC_SECRET_KEY
        self.base_url = Config.MEXC_BASE_URL

    def _sign_request(self, params):
        """Generate a signed request for MEXC API"""
        query_string = "&".join([f"{key}={params[key]}" for key in sorted(params)])
        signature = hmac.new(self.secret_key.encode(), query_string.encode(), hashlib.sha256).hexdigest()
        return signature

    def get_account_info(self):
        """Fetch account balance"""
        endpoint = "/api/v3/account"
        url = self.base_url + endpoint
        timestamp = int(time.time() * 1000)

        params = {
            "timestamp": timestamp
        }
        params["signature"] = self._sign_request(params)

        headers = {"X-MEXC-APIKEY": self.api_key}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def place_order(self, symbol, side, quantity, price):
        """Place a limit order"""
        endpoint = "/api/v3/order"
        url = self.base_url + endpoint
        timestamp = int(time.time() * 1000)

        params = {
            "symbol": symbol,
            "side": side.upper(),
            "type": "LIMIT",
            "quantity": quantity,
            "price": price,
            "timestamp": timestamp
        }
        params["signature"] = self._sign_request(params)

        headers = {"X-MEXC-APIKEY": self.api_key}
        response = requests.post(url, headers=headers, params=params)
        return response.json()
