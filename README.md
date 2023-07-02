# Alpha Vantage Wrapper

This Python module provides an easy-to-use wrapper for the Alpha Vantage API, which allows you to fetch financial market data.

## Features

- Fetch intraday stock price data for a specific stock symbol

## Requirements

- Python 3.7 or newer
- pandas library
- requests library

## Installation

To install the Alpha Vantage Wrapper, you can use pip:

```bash
pip install -r requirements.txt
```

## Usage (Main.py)

```python
from alphavantage_wrapper.api import AlphaVantageAPI
import os

api_key = os.getenv('ALPHA_VANTAGE_API_KEY')  # set your actual API KEY as an enviroment variable
alpha_vantage = AlphaVantageAPI(api_key)
df = alpha_vantage.get_intraday_stock_data('AAPL', '60min')
print(df)
```

```bash
python main.py
```
