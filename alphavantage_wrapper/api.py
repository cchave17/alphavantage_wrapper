import requests
import time
import pandas as pd

class AlphaVantageAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query?"

    def get_intraday_stock_data(self, symbol, interval='60min'):
        """Fetches the intraday stock price data for a specific stock symbol."""
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': symbol,
            'interval': interval,
            'apikey': self.api_key,
            'outputsize': 'full',  # get as much data as the API allows
            'datatype': 'json'
        }
        response = self.send_request(params)
        data = response.json()

        try:
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
        except KeyError:
            print("An error occurred. Here is the response data:")
            print(data)


    def send_request(self, params):
        """Sends the request and handles potential API rate limit errors."""
        response = requests.get(self.base_url, params=params)
        if response.status_code != 200:
            raise Exception(f"Request failed with status {response.status_code}")
        return response
