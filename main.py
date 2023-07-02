from alphavantage_wrapper.api import AlphaVantageAPI
import os
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
alpha_vantage = AlphaVantageAPI(api_key)
df = alpha_vantage.get_intraday_stock_data('AAPL', '60min')
print(df)
