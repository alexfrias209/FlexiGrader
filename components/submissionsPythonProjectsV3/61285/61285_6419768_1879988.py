import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('61285_6419767_5850317.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

print(df.describe())

fig, ax1 = plt.subplots(figsize=(14, 7))
color = 'tab:blue'
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Prices', color=color)
ax1.plot(df.index, df['Close'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Volume', color=color)
ax2.plot(df.index, df['Volume'], color=color)
ax2.tick_params(axis='y', labelcolor=color)
plt.show()

short_window = 40
long_window = 100

signals = pd.DataFrame(index=df.index)
signals['price'] = df['Close']
signals['short_mavg'] = df['Close'].rolling(window=short_window).mean()
signals['long_mavg'] = df['Close'].rolling(window=long_window).mean()

plt.figure(figsize=(14, 7))
plt.plot(signals.index, signals['price'], label='Price')
plt.plot(signals.index, signals['short_mavg'], label='40-days MA')
plt.plot(signals.index, signals['long_mavg'], label='100-days MA')
plt.legend()
plt.show()

df['Log_Return'] = np.log(df['Close'] / df['Close'].shift(1))
volatility = df['Log_Return'].rolling(window=252).std() * np.sqrt(252)
plt.figure(figsize=(14, 7))
volatility.plot()
plt.show()
