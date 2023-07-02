import requests
import time
import pandas as pd
from .exceptions import APIError, RateLimitError, ResponseError

class AlphaVantageAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query?"

    def get_historical_stock_data(self, symbol, interval='daily'):
        """Fetches the historical stock price data for a specific stock symbol."""
        function = 'TIME_SERIES_' + interval.upper()
        params = {
            'function': function,
            'symbol': symbol,
            'apikey': self.api_key,
            'outputsize': 'full',  # get the full-length time series of up to 20 years of historical data
            'datatype': 'json'
        }
        response = self.send_request(params)
        data = response.json()

        if "Note" in data and "API call frequency" in data["Note"]:
            raise RateLimitError("API request limit reached. Please wait before making more requests.")

        if 'Time Series ({interval})' not in data:
            raise ResponseError("The API response is not in the expected format.")

        df = pd.DataFrame(data[f'Time Series ({interval})']).T
        df = df.rename(columns={
            '1. open': 'open',
            '2. high': 'high',
            '3. low': 'low',
            '4. close': 'close',
            '5. volume': 'volume'
        })
        df.index = pd.to_datetime(df.index)
        return df

    def send_request(self, params):
        """Sends the request and handles potential API rate limit errors."""
        response = requests.get(self.base_url, params=params)
        if response.status_code != 200:
            raise APIError(f"Request failed with status {response.status_code}")
        return response