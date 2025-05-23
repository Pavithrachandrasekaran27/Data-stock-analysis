import matplotlib.pyplot as plt
import seaborn as sns

def plot_volatility(df):
    volatility = df.groupby('symbol')['daily_return'].std().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    volatility.plot(kind='bar')
    plt.title("Top 10 Most Volatile Stocks")
    plt.ylabel("Std Dev of Daily Returns")
    plt.tight_layout()
    plt.show()

def plot_sector_performance(df, sector_map):
    df = df.merge(sector_map, on='symbol')
    df['yearly_return'] = df.groupby('symbol')['cumulative_return'].transform('last') - 1
    sector_avg = df.groupby('sector')['yearly_return'].mean()
    sector_avg.plot(kind='bar', figsize=(10,6), title="Avg Return by Sector")
    plt.ylabel("Average Return")
    plt.tight_layout()
    plt.show()

def plot_correlation_heatmap(df):
    pivot_df = df.pivot_table(index='date', columns='symbol', values='close')
    corr = pivot_df.pct_change().corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr, cmap='coolwarm', center=0)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()
