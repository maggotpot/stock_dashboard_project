# Stock Performance & Risk Analytics Dashboard

## Project Overview
This project analyzes historical stock price data to evaluate performance and risk.
The goal is to calculate key financial metrics and visualise insights through an interactive dashboard.

## Tools & Technologies
- Python
- Pandas & NumPy
- yFinance API
- Plotly & Matplotlib
- Streamlit (for dashboard)

## Methodology
1. Download historical adjusted closing prices using yFinance
2. Calculate daily returns and cumulative returns
3. Compute volatility and Sharpe ratio
4. Visualize trends and risk metrics
5. Build an interactive dashboard to communicate insights

## Explanation of Key Metrics
- DAILY RETURNS: Percentage change in stock prices
- VOLATILITY: Standard deviation of returns (annualized)
- SHARPE RATIO: Risk-adjusted return measure

## Results & Insights
- Price trends differ significanlty across stocks, showing long run changes in growth patterns and drawdown behavior.
- Returns were normalized using percentage changes, ensuring comparison between assets with different price levels.
- Volatility varies considerably across stocks.
- Higher returns are often accompanied by higher risk.
- Lower-volatility assets often achieve high Sharpe ratios, showing more efficient compensation for risk taken.
- Risk-adjusted metrics provide superior investment insight compared to just raw returns.

## How to Run the Project
```bash
pip install -r requirements.txt
streamlit run dashboard.py

