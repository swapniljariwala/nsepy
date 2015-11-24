# nsepy
Python Library to get publicly available data on NSE website ie. stock quotes, historical data, live indices 

##Libraries Required
- requests
- beautifulsoup
- numpy 
- scipy
- pandas

For Windows systems you can install Anaconda, this will cover many dependancies (You'll have to install requests and beautifulsoup additionally though)

##Installation
```$pip install nsepy```
##Usage

Get the price history of stocks and NSE indices directly in pandas dataframe-
```python
from nsepy.archives import get_price_history
from nsepy import indices
from datetime import date
#Stock price history
sbin = get_price_history(stock = 'SBIN',
                        start = date(2015,1,1), 
                        end = date(2015,1,10))
sbin[[ 'VWAP', 'Turnover']].plot(secondary_y='Turnover')
#Index price history
nifty = indices.archives.get_price_history(index = "NIFTY 50", 
                                            start = date(2015,9,1), 
                                            end = date(2015,9,24))
nifty[['Close', 'Turnover']].plot(secondary_y='Turnover')
#Index P/E ratio history
nifty_pe = indices.archives.get_price_history(index = "NIFTY 50", 
                                            start = date(2015,9,1), 
                                            end = date(2015,9,24))
nifty_pe['Index'] = nifty['Close']
nifty_pe[['Index', 'P/E']].plot(secondary_y='P/E')
```
To do-
1. Adding tests
2. Unifying get_price_history for all segments (stock, indices, derivative)
3. Support for live data
[Visit my blog to explore other projects](http://www.xerxys.in)
