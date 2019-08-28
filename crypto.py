import pandas as pd
import pandas_datareader.data as pdr
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# set the end time for today's date
end = datetime.today()

# set the start time for a year from today
start = datetime(end.year - 1, end.month, end.day)

# Pull crypto data from yahoo and anaylyze it between date variables
BTC = pdr.DataReader('BTC-USD', 'yahoo', start, end)
# print(BTC)

ETH = pdr.DataReader('ETH-USD', 'yahoo', start, end)
# print(ETH)

LTC = pdr.DataReader('LTC-USD', 'yahoo', start, end)
# print(LTC)

XRP = pdr.DataReader('XRP-USD', 'yahoo', start, end)
# print(XRP)

# Plot The closing price data on a
# ETH['Adj Close'].plot(legend = True)

# Moving averages
ma_days = [10, 20, 50]
for ma in ma_days: 
    column_name = "MA %s days" % (str(ma))
    BTC[column_name] = BTC['Adj Close'].rolling(window=ma, center=False).mean()
BTC[['Adj Close', 'MA 10 days', 'MA 20 days', 'MA 50 days']].plot(legend=True)

# Show the plot
plt.show()
