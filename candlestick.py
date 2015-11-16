#!/usr/bin/env python
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator,\
     DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc
from nsepy.archives import get_price_history
from datetime import date
import pandas as pd
import matplotlib.dates as mdates

# example from - http://matplotlib.org/examples/pylab_examples/finance_demo.html

start = date(2015,9,1)
end = date(2015,9,21)

mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12
#proxies = {'http':'proxy1.wipro.com:8080'}

df = get_price_history(stock='SBIN', start=start, 
                      end = end)
                      
df["Date"] = pd.to_datetime(df.index)
df.Date = mdates.date2num(df.Date.dt.to_pydatetime())
quotes = [tuple(x) for x in df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']].to_records(index=False)]


#quotes = quotes_historical_yahoo_ohlc('INTC', date1, date2)
if len(quotes) == 0:
    raise SystemExit

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
#ax.xaxis.set_minor_formatter(dayFormatter)

#plot_day_summary(ax, quotes, ticksize=3)
candlestick_ohlc(ax, quotes, width=0.6)

ax.xaxis_date()
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()