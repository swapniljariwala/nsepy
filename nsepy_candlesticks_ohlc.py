#Importing Libraries
from nsepy import get_history
from datetime import date, timedelta
from nsepy import get_index_pe_history

from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

#TICKER NAME
ticker = "MCDOWELL-N"

#TIME PERIOD, 15 days in this case
end_day = date.today()
start_day = end_day - timedelta(15)

#Fetch ticker data from nsepy
df = get_history(symbol=ticker, start=start_day, end=end_day)

#Data preparation for OHLC Candlesticks
data=df[['Open', 'High', 'Low', 'Close', 'Volume']]
#print(data)
data.index.name = 'Date'



#mplfinance
import mplfinance as mpf
from mplfinance.original_flavor import candlestick_ohlc
data.index = pd.to_datetime(data.index)
mpf.plot(data, type='candle', volume=True)





