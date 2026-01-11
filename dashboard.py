import streamlit as st
import plotly.express as px
import pandas as pd

from analysis import (get_price_data, calculate_daily_returns,
                      calculate_cumulative_returns, calculate_volatility,
                      calculate_sharpe_ratio)   

st.set_page_config(page_title="Stock Performance Dashboard", layout="wide")

st.title("Stock Performance & Risk Analytics Dashboard")
st.write("Analyze stock performance, risk, and risk-adjusted returns.")



stocks = ["AAPL", "MSFT", "GOOGL", "AMZN", "SPY"]

selected_stocks = st.multiselect(
    "Select stocks to analyze:",
    stocks,
    default=["AAPL", "MSFT", "SPY"]
)

start_date = st.date_input("Start Date", value=pd.to_datetime("2019-01-01"))
end_date = st.date_input("End Date", value=pd.to_datetime("today"))

if selected_stocks:
    prices = get_price_data(selected_stocks, start_date, end_date)
    daily_returns = calculate_daily_returns(prices)
    cumulative_returns = calculate_cumulative_returns(daily_returns)
    volatility = calculate_volatility(daily_returns)
    sharpe_ratio = calculate_sharpe_ratio(daily_returns)

    st.subheader("Stock Price Trends")
    price_chart = px.line(prices, title="Adjusted Closing Prices")
    st.plotly_chart(price_chart, use_container_width=True)

    st.subheader("Cumulative Returns")
    cumret_chart = px.line(cumulative_returns, title="Cumulative Returns")
    st.plotly_chart(cumret_chart, use_container_width=True)

    st.subheader("Risk & Performance Metrics")

    metrics = pd.DataFrame({
        "Volatility": volatility,
        "Sharpe Ratio": sharpe_ratio
    })

    st.dataframe(metrics.style.format("{:.2f}"))