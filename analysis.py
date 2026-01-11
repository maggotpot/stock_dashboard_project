import yfinance as yf
import pandas as pd
import numpy as np

def get_price_data(tickers, start_date, end_date):
    """
    Downloads adjusted closing prices for selected stocks.
    Robust to yfinance / pandas format differences.
    """

    data = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        group_by="column",
        auto_adjust=False,
        progress=False
    )

    # Case 1: MultiIndex columns (most common for multiple tickers)
    if isinstance(data.columns, pd.MultiIndex):
        if "Adj Close" in data.columns.levels[0]:
            price_data = data["Adj Close"]
        elif "Close" in data.columns.levels[0]:
            price_data = data["Close"]
        else:
            raise KeyError("Neither 'Adj Close' nor 'Close' found in data")

    # Case 2: Single ticker, flat columns
    else:
        if "Adj Close" in data.columns:
            price_data = data[["Adj Close"]]
        elif "Close" in data.columns:
            price_data = data[["Close"]]
        else:
            raise KeyError("Neither 'Adj Close' nor 'Close' found in data")

    # Ensure columns are ticker symbols
    if isinstance(tickers, list):
        price_data.columns = tickers
    else:
        price_data.columns = [tickers]

    return price_data

def calculate_daily_returns(price_data):
    '''Calculate daily percentage returns.'''
    return price_data.pct_change().dropna()

def calculate_cumulative_returns(daily_returns):
    '''Calculate cumulative returns over time.'''
    return (1 + daily_returns).cumprod() - 1

def calculate_volatility(daily_returns):
    '''Annualized volatility using 252 trading days.'''
    return daily_returns.std() * np.sqrt(252)

def calculate_sharpe_ratio(daily_returns, risk_free_rate=0.03):
    '''Calculate annualized Sharpe Ratio.'''
    annual_returns = daily_returns.mean() * 252
    volatility = calculate_volatility(daily_returns)
    sharpe_ratio = (annual_returns - risk_free_rate) / volatility
    return sharpe_ratio