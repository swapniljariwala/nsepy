# nsepy
Python Library to get publicly available data on NSE website ie. stock quotes, historical data, live indices 

##Libraries Required
- requests
- beautifulsoup
- numpy 
- scipy
- pandas

For Windows systems you can install Anaconda, this will cover many dependancies (You'll have to install requests and beautifulsoup additionally though)
##Usage
Store data directly to csv using simple functions
Until I package this as library, this tool can be used with below directory structure-
-->Code_Directory/
    |
    -->nsepy/
    |   |
    |   -->archives.py
    |   |
    |   -->derivatives/
    |   |
    |   -->indices/
    |
    -->explot.py, excsv.py
    
```python

from nsepy.archives import get_price_history_csv

with open('sbin.csv','w') as fp:
    #options for period '1month', '3months', '1week'
    get_price_history_csv(fp, 'SBIN', period = '1month') 

with open('LT.csv','w') as fp:
    get_price_history_csv(fp, 'LT', start = '01-01-2014', end = '20-01-2014',
        proxies = {'http': 'proxy.domain:port'})
```
You can get output in pandas dataframe directly, ready for analysis
```python
from nsepy.archives import get_price_history
d = get_price_history(stock = 'LT',start = '01-01-2014', end = '20-01-2014', 
                          proxies = {'http': 'proxy.domain:port'})
d[['high_price', 'vwap', 'low_price']].plot()
```

[Visit my blog to explore other projects](http://www.xerxys.in)
