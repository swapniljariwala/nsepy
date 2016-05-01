.. NSEpy documentation master file, created by
   sphinx-quickstart on Mon Dec 14 00:10:20 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

NSEpy
=====
NSEpy is a library to extract historical and realtime data from NSE's website. This Library aims to keep the API very simple.

Python is a great tool for data analysis along with the scipy stack and the main objective of NSEpy is to provide analysis ready data-series for use with scipy stack. NSEpy can seamlessly integrate with Technical Analysis library (Acronymed TA-Lib, includes 200 indicators like MACD, RSI). This library would serve as a basic building block for automatic/semi-automatic algorithm trading systems or backtesting systems for Indian markets.

Quick Start
-----------

Installation
~~~~~~~~~~~~

`$ pip install nsepy`

Quick Hand-On
~~~~~~~~~~~~~
Here's a simple example to get historical stock data for the month of January 2015.

>>> from nsepy import get_history
>>> from datetime import date
>>> start = date(2015,1,1)
>>> end = date(2015,1,31)
>>> data = get_history(symbol="SBIN", start=start, end=end)
>>> data[['Close']].plot()


Get the price history of stocks and NSE indices directly in pandas dataframe::


	from nsepy import get_history, get_index_pe_history
	from datetime import date
	"""
		get_history argument list
				symbol (str): Symbol for stock (SBIN, RELIANCE etc.), index (NIFTY, BANKNIFTY etc) or any security (Index names "NIFTY 50", "INDIAVIX" etc.
				start (datetime.date): start date 
	            end (datetime.date): end date
	            index (boolean): False by default, True if its an index, index futures or options and also for INDIAVIX
	            futures (boolean): False by default, True for index and stock futures only (should not be set to True with option_type specified)
	            expiry_date (datetime.date): Expiry date for derivatives, Compulsory parameter for futures and options
	            option_type (str): It takes "CE", "PE", "CA", "PA" for European and American calls and puts
	            strike_price (int): Strike price, Compulsory parameter for options
	            series (str): Defaults to "EQ", but can be "BE" etc (refer NSE website for details)
	"""
	
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
	
	#Futures and Options historical data
	nifty_fut = get_history(symbol="NIFTY", 
							start=date(2015,1,1), 
							end=date(2015,1,10),
							index=True,
							futures=True, expiry_date=date(2015,1,29))
							
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

Sample contents of the one of the dataframe (I'm using Anaconda and Spyder)

>>> nifty_fut
>>>     	Symbol      Expiry     Open    High      Low    Close     Last  
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



Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

