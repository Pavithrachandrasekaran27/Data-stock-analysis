import streamlit as st
import pandas as pd
from analysis import load_all_stock_data, calculate_returns, market_summary
from visualization import plot_volatility, plot_sector_performance, plot_correlation_heatmap

st.title("📈 Stock Performance Dashboard")

csv_folder = "data/csv_output"
sector_map = pd.read_csv("data/sector_map.csv")

st.write("Loading and analyzing stock data...")
df = load_all_stock_data(csv_folder)
df = calculate_returns(df)

if st.checkbox("Show Market Summary"):
    summary = market_summary(df)
    st.dataframe(summary.head(10))

if st.checkbox("Plot Volatility"):
    plot_volatility(df)

if st.checkbox("Plot Sector Performance"):
    plot_sector_performance(df, sector_map)

if st.checkbox("Correlation Heatmap"):
    plot_correlation_heatmap(df)

st.success("Dashboard Ready")
