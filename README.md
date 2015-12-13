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
from nsepy import get_history, get_index_pe_history
from datetime import date
sbin = get_history(symbol = 'SBIN',
                    start = date(2015,1,1), 
                    end = date(2015,1,10))
sbin[[ 'VWAP', 'Turnover']].plot(secondary_y='Turnover')

#Index price history
nifty = get_history(symbol = "NIFTY", 
                    start = date(2015,1,1), 
                    end = date(2015,1,10),
					index=True)
nifty[['Close', 'Turnover']].plot(secondary_y='Turnover')

#Index futures history
nifty_fut = get_history(symbol="NIFTY", 
						start=date(2015,1,1), 
						end=date(2015,1,10),
						index=True,
						futures=True, expiry_date=date(2015,1,29))

#Stock options history
stock_opt = get_history(symbol="SBIN",
						start=date(2015,1,1), 
						end=date(2015,1,10),
						option_type="CE",
						strike_price=300,
						expiry_date=date(2015,1,29))

#Index P/E ratio history
nifty_pe = get_index_pe_history(symbol="NIFTY",
								start=date(2015,1,1), 
								end=date(2015,1,10))
```
Sample contents of the one of the dataframe (I'm using Anaconda and Spyder)-
```
In[6]: nifty_fut
Out[6]: 
           Symbol      Expiry     Open    High      Low    Close     Last  Date                                                                        
2015-01-01  NIFTY  2015-01-29  8320.00  8356.0  8295.20  8343.80  8347.05   
2015-01-02  NIFTY  2015-01-29  8352.25  8470.9  8352.25  8458.40  8468.00   
2015-01-05  NIFTY  2015-01-29  8452.35  8492.0  8406.00  8422.85  8423.85   
2015-01-06  NIFTY  2015-01-29  8422.00  8422.0  8000.00  8157.90  8150.30   
2015-01-07  NIFTY  2015-01-29  8150.00  8184.0  8096.00  8141.85  8154.00   
2015-01-08  NIFTY  2015-01-29  8209.00  8274.9  8193.10  8257.25  8255.00   
2015-01-09  NIFTY  2015-01-29  8306.35  8334.0  8205.00  8315.50  8311.60   

            Settle Price  Number of Contracts      Turnover  Open Interest  Date                                                                         
2015-01-01       8343.80               152053  3.165350e+10       21140550   
2015-01-02       8458.40               384440  8.105711e+10       21427925   
2015-01-05       8422.85               362889  7.661895e+10       20698500   
2015-01-06       8157.90               807830  1.663583e+11       19157775   
2015-01-07       8141.85               513814  1.046381e+11       18716025   
2015-01-08       8257.25               409705  8.433153e+10       17798500   
2015-01-09       8315.50               596384  1.234251e+11       17111350   

            Change in OI  Underlying  
Date                                  
2015-01-01        -28675     8284.00  
2015-01-02        287375     8395.45  
2015-01-05       -729425     8378.40  
2015-01-06      -1540725     8127.35  
2015-01-07       -441750     8102.10  
2015-01-08       -917525     8234.60  
2015-01-09       -687150     8284.50  
```


Below functions still work but these will be depricated soon
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
nifty_pe = indices.archives.get_pe_history(index = "NIFTY 50", 
                                            start = date(2015,9,1), 
                                            end = date(2015,9,24))
nifty_pe['Index'] = nifty['Close']
nifty_pe[['Index', 'P/E']].plot(secondary_y='P/E')
```
To do-
* Unifying get_price_history for all segments (stock, indices, derivative)
* Support for live data
* Tests and Python compatibility between 3 and 2


[Visit my blog to explore other projects](http://www.xerxys.in)
