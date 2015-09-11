# nsepy
Python Library to get publicly available data on NSE website ie. stock quotes, historical data, live indices 

##Usage
```python

from archives import get_price_history_csv

with open('sbin.csv','w') as fp:
    #options for period '1month', '3months', '1week'
    get_price_history_csv(fp, 'SBIN', period = '1month') 

with open('LT.csv','w') as fp:
    get_price_history_csv(fp, 'LT', start = '01-01-2014', end = '20-01-2014')
```

[Visit my blog to explore other projects](http://www.xerxys.in)
