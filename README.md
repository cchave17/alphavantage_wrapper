# Alpha Vantage Wrapper

This project is a Python wrapper for the Alpha Vantage API. It allows for easy access and manipulation of financial data, including historical stock price data, real-time stock price data, Forex data, cryptocurrency data, and technical indicators. 

## Features

- Fetch historical stock price data
- Fetch real-time stock price data
- Fetch Forex data
- Fetch cryptocurrency data
- Fetch technical indicators
- Fetch sector performance data
- Handle API rate limits

## Installation

To install the Alpha Vantage Wrapper, you can use pip:

```bash
pip install alphavantage_wrapper
```

## Usage

```python
from alphavantage_wrapper import AlphaVantageAPI

api = AlphaVantageAPI(api_key='DJNJJYE2WYUEL1LU')

# Get historical stock data
data = api.get_historical_stock_data('AAPL', '2020-01-01', '2020-12-31')

# Get real-time stock data
data = api.get_real_time_stock_data('AAPL')

# ... (other examples)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)