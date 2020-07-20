# NSEpy 0.8
Python Library to get publicly available data on NSE website ie. stock quotes, historical data, live indices.

Detailed documentation here - https://nsepy.xyz/

Release Notes
* Added support for derivative data. (Probably only API for indian derivative and India VIX data as Yahoo API has no support for derivatives)
* Support for RBI reference rates for USD
* Download data thru simple cli
* Unified and simplified API for all (Equity, Index, Derivative, Volatility Indexes-INDIAVIX)
* Compatible and Tested with Python 2.7 and 3.4

## Libraries Required
- requests
- beautifulsoup
- numpy 
- scipy
- pandas
- lxml

For Windows systems you can install Anaconda, this will cover many dependancies (You'll have to install requests and beautifulsoup additionally though)

## Installation
Fresh installation 

```$pip install nsepy```

Upgrade

```$pip install nsepy --upgrade```

## Usage

Get the price history of stocks and NSE indices directly in pandas dataframe-
```python

#Stock history
sbin = get_history(symbol='SBIN',
                    start=date(2015,1,1), 
                    end=date(2015,1,10))
sbin[[ 'VWAP', 'Turnover']].plot(secondary_y='Turnover')

"""	Index price history
	symbol can take these values (These indexes have derivatives as well)
	"NIFTY" or "NIFTY 50",
	"BANKNIFTY" or "NIFTY BANK",
	"NIFTYINFRA" or "NIFTY INFRA",
    	"NIFTYIT" or "NIFTY IT",
    	"NIFTYMID50" or "NIFTY MIDCAP 50",
    	"NIFTYPSE" or "NIFTY PSE"
	In addition to these there are many indices
	For full list refer- http://www.nseindia.com/products/content/equities/indices/historical_index_data.htm
"""
nifty = get_history(symbol="NIFTY", 
                    start=date(2015,1,1), 
                    end=date(2015,1,10),
					index=True)
nifty[['Close', 'Turnover']].plot(secondary_y='Turnover')


```
Sample contents of the one of the dataframe (I'm using Anaconda and Spyder)-
```
In[6]: nifty_fut
Out[6]: 
           Symbol      Expiry     Open    High      Low    Close     Last  
Date                                                                        
2015-01-01  NIFTY  2015-01-29  8320.00  8356.0  8295.20  8343.80  8347.05   
2015-01-02  NIFTY  2015-01-29  8352.25  8470.9  8352.25  8458.40  8468.00   
2015-01-05  NIFTY  2015-01-29  8452.35  8492.0  8406.00  8422.85  8423.85   
2015-01-06  NIFTY  2015-01-29  8422.00  8422.0  8000.00  8157.90  8150.30   
2015-01-07  NIFTY  2015-01-29  8150.00  8184.0  8096.00  8141.85  8154.00   
2015-01-08  NIFTY  2015-01-29  8209.00  8274.9  8193.10  8257.25  8255.00   
2015-01-09  NIFTY  2015-01-29  8306.35  8334.0  8205.00  8315.50  8311.60   

            Settle Price  Number of Contracts      Turnover  Open Interest  
Date                                                                         
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


## How can I contribute?
There are multiple ways in which you can contribute-

### Write about your project

I'm putting about 1 Hr per week on NSEpy as hobby and I will continue to do so. but as this effort is just not enough, NSEpy at the moment is short of good documentation. There are lot of features in NSEpy still not documented :( , so till we complete the documentation, I'll need support from the community.

Please write about your projects in blogs, quora answers and other forums, so that people find working examples to get started.

### Raising issues, bugs, enhancement requests

For quick resolution please raise issues both [here on issue page](https://github.com/swapniljariwala/nsepy/issues) as well as on [Stackoverflow](https://stackoverflow.com/). I'll try my best to address the issues quickly on github as and when I get notified, but raising it on stackoverflow will provide you access to a larger group and someone else might solve your problem before I do.

### Submit patches

If you have fixed an issue or added a new feature, please fork this repository, make your changes and submit a pull request. [Here's good article on how to do this.](https://code.tutsplus.com/tutorials/how-to-collaborate-on-github--net-34267) 

Looking forward for healthy participation from community.
