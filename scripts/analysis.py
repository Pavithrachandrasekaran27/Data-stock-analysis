import pandas as pd
import numpy as np
import glob
import os

def load_all_stock_data(csv_folder):
    all_data = []
    for file in glob.glob(f"{csv_folder}/*.csv"):
        df = pd.read_csv(file)
        df['symbol'] = os.path.basename(file).replace('.csv', '')
        df['date'] = pd.to_datetime(df['date'])
        all_data.append(df)
    return pd.concat(all_data)

def calculate_returns(df):
    df.sort_values(by=['symbol', 'date'], inplace=True)
    df['daily_return'] = df.groupby('symbol')['close'].pct_change()
    df['cumulative_return'] = (1 + df['daily_return']).groupby(df['symbol']).cumprod()
    return df

def market_summary(df):
    yearly_return = df.groupby('symbol').apply(lambda x: (x['close'].iloc[-1] - x['close'].iloc[0]) / x['close'].iloc[0])
    return yearly_return.sort_values(ascending=False)
