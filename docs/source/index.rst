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
>>> data = get_history(symbol="SBIN", start=date(2015,1,1), end=date(2015,1,31))
>>> data[['Close']].plot()

Fetching Price History
------------------------
Function `get_history` fetches the price history of stocks/indices/derivatives and returns a pandas dataframe.

Stock price history
~~~~~~~~~~~~~~~~~~~
::
    
    from datetime import date
    from nsepy import get_history
    sbin = get_history(symbol='SBIN',
                       start=date(2015,1,1), 
                       end=date(2015,1,10))

Executed on ipython console::
    
    In [1]: sbin
    Out[1]:     Symbol Series  Prev Close    Open    High     Low   Last   Close  \
    Date                                                                          
    2015-01-01   SBIN     EQ      311.85  312.45  315.00  310.70  314.0  314.00   
    2015-01-02   SBIN     EQ      314.00  314.35  318.30  314.35  315.6  315.25   
    2015-01-05   SBIN     EQ      315.25  316.25  316.80  312.10  312.8  312.75   
    2015-01-06   SBIN     EQ      312.75  310.00  311.10  298.70  299.9  299.90   
    2015-01-07   SBIN     EQ      299.90  300.00  302.55  295.15  301.4  300.15   

                  VWAP    Volume      Turnover  Trades  Deliverable Volume  \
    Date                                                                     
    2015-01-01  313.67   6138488  1.925489e+14   58688             1877677   
    2015-01-02  316.80   9935094  3.147389e+14   79553             4221685   
    2015-01-05  313.84   9136716  2.867432e+14   88236             3845173   
    2015-01-06  305.14  15329257  4.677601e+14  169268             7424847   
    2015-01-07  299.95  15046745  4.513243e+14  147185             5631400   

                %Deliverble  
    Date                     
    2015-01-01       0.3059  
    2015-01-02       0.4249  
    2015-01-05       0.4208  
    2015-01-06       0.4844  
    2015-01-07       0.3743  


Stock futures price history
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set `futures=True` and provide `expiry_date` of the contract (Refer :ref:`get_expiry_date`) ::
    
    from datetime import date
    from nsepy import get_history
    # Stock options (Similarly for index options, set index = True)
    stock_fut = get_history(symbol="SBIN",
                            start=date(2015,1,1), 
                            end=date(2015,1,10),
                            futures=True,
                            expiry_date=date(2015,1,29))

Please refer to Note on :ref:`zero_values_in_derivatives`.
                            
When executed the above code on ipython console::

    In [38]: stock_opt
    Out[38]: 
               Symbol      Expiry    Open    High     Low   Close    Last  \
    Date                                                                    
    2015-01-01   SBIN  2015-01-29  315.10  317.95  313.40  316.65  317.00   
    2015-01-02   SBIN  2015-01-29  317.50  320.95  317.10  317.75  318.30   
    2015-01-05   SBIN  2015-01-29  318.00  318.75  314.10  315.00  315.05   
    2015-01-06   SBIN  2015-01-29  312.95  312.95  300.10  301.30  301.10   
    2015-01-07   SBIN  2015-01-29  301.95  304.55  297.35  302.25  303.50   
    2015-01-08   SBIN  2015-01-29  306.50  308.40  303.70  306.65  307.00   
    2015-01-09   SBIN  2015-01-29  306.75  309.25  301.05  304.75  304.15   

                Settle Price  Number of Contracts      Turnover  Open Interest  \
    Date                                                                         
    2015-01-01        316.65                14720  5.821172e+09       55480000   
    2015-01-02        317.75                22525  8.988242e+09       55087500   
    2015-01-05        315.00                17455  6.898723e+09       55718750   
    2015-01-06        301.30                29338  1.126715e+10       56701250   
    2015-01-07        302.25                28489  1.074823e+10       58036250   
    2015-01-08        306.65                20120  7.702653e+09       57287500   
    2015-01-09        304.75                18961  7.247211e+09       57035000   

                Change in OI  Underlying  
    Date                                  
    2015-01-01        358750      314.00  
    2015-01-02       -392500      315.25  
    2015-01-05        631250      312.75  
    2015-01-06        982500      299.90  
    2015-01-07       1335000      300.15  
    2015-01-08       -748750      304.85  
    2015-01-09       -252500      303.20


Stock options price history
~~~~~~~~~~~~~~~~~~~~~~~~~~~
For stock options, specify- 

* `option_type` as "CE" for call and as "PE" for put option
* `strike_price` - the strike price of the contract
* `expiry_date` - expiry date of the contract, refer:ref:`get_expiry_date`. ::
    
    # Stock options (Similarly for index options, set index = True)
    stock_opt = get_history(symbol="SBIN",
                            start=date(2015,1,1), 
                            end=date(2015,1,10),
                            option_type="CE",
                            strike_price=300,
                            expiry_date=date(2015,1,29))

Index price history
~~~~~~~~~~~~~~~~~~~
There are currently 50+ indices maintained by NSE. You can get historical data for all of them.::
Usage-

* `symbol` - Name of the index in capital `(Refer this page for list of indices) <https://www.nseindia.com/products/content/equities/indices/historical_index_data.htm>`_
* `index` - Set this True for all index related operations ::
                          
    # NIFTY Next 50 index
    nifty_next50 = get_history(symbol="NIFTY NEXT 50",
                                start=date(2015,1,1), 
                                end=date(2015,1,10),
                                index=True)
    # NIFTY50 Equal wight index (random index from the list)
    nifty_eq_wt = get_history(symbol="NIFTY50 EQUAL WEIGHT",
                                start=date(2017,6,1), 
                                end=date(2017,6,10),
                                index=True)
You will observe a lot of NaN values for many indeces like 'NIFTY50 Equal wight index', In those cases just use 'Close' values 

Index futures price history
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Out of the 60+ indices, only 7 indeces are available for derivative. (`List available here. <https://www.nseindia.com/products/content/derivatives/equities/fo_underlying_home.htm>`_)
Usage-

* `index` - Set True
* `futures` - Set True
* `expiry_date` - Expiry date of the contract. refer:ref:`get_expiry_date`. ::

    nifty_fut = get_history(symbol="NIFTY", 
                            start=date(2015,1,1), 
                            end=date(2015,1,10),
                            index=True,
                            futures=True,
                            expiry_date=date(2015,1,29))

Index options price history
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Usage-

* `index` - Set True
* `option_type` as "CE" for call and as "PE" for put option
* `strike_price` - the strike price of the contract
* `expiry_date` - expiry date of the contract, refer:ref:`get_expiry_date`. ::
                            
    nifty_opt = get_history(symbol="NIFTY", 
                            start=date(2015,1,1), 
                            end=date(2015,1,10),
                            index=True,
                            option_type='CE',
                            strike_price=8200,
                            expiry_date=date(2015,1,29))


India VIX price history
~~~~~~~~~~~~~~~~~~~~~~~
India VIX is a volatility index which gives a measurement of market volatility based on NIFTY options contract. This servers as important parameter in option pricing. ::
                            
	vix = get_history(symbol="INDIAVIX", 
                    start=date(2015,1,1), 
                    end=date(2015,1,10),
                    index=True)


.. _zero_values_in_derivatives:

Missing or zero values in derivative data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 Although `NSE specifies <https://www.nseindia.com/products/content/derivatives/equities/contract_specifitns.htm>`_ a trading cycle of three months, most stock futures will not be traded for whole three months, rather they will be active only in the month of expiry, So you may get 0 values for days when no contracts were traded. Please deal with this situation carefully in your logic.

.. _get_expiry_date:
    
Fetching Expiry Dates
---------------------
Fetch expiry date of all derivative contracts for a perticular month and year. 
Usage-

* month - Month of contract expiry starting from 1 for January and 12 for December
* year - Year of the contract expiry ::

    from nsepy.derivatives import get_expiry_date
    expiry = get_expiry_date(year=2015, month=1)

Use this function with `get_history`::

    stock_opt = get_history(symbol="SBIN",
                                start=date(2015,1,1), 
                                end=date(2015,1,10),
                                futures=True,
                                expiry_date=get_expiry_date(2015,1))


Index P/E Ratio History
-----------------------
P/E ratio of a security helps to estimate if the security is over-priced or under-priced. NSE offers historical P/E ratio for 30+ thematic and sectoral indices, we can use this data to determine which sectors are over-priced or under-priced and further make investment decisions. ::

    # Index P/E ratio history
    from nsepy import get_index_pe_history
    nifty_pe = get_index_pe_history(symbol="NIFTY",
                                    start=date(2015,1,1), 
                                    end=date(2015,1,10))


RBI Reference Rates
-------------------
USD, GBP, EURO, YEN to INR rbi reference rates::

    from nsepy import get_rbi_ref_history
    rbi_ref = get_rbi_ref_history(date(2015,1,1), date(2015,1,10))


Daily Bhav Copy
---------------
Download daily bhav copy, which is nothing but OHLC prices of all the traded stocks on a particular day::

    from nsepy.history import get_price_list    
    prices = get_price_list(dt=date(2015,1,1))

Command Line Interface
----------------------
NSEpy offers a simple to use, easy to remember command line interface, This method is useful when you just want the data for further processed in Excel, R or any other tool which supports CSV format.
Basic Use, Fetch stock price history ::
    
$ nsecli history --symbol SBIN -s 2017-01-01 -e 2017-01-31 -o output.csv

This will save price history of State Bank of India for the month of January 2017 as csv file with name output.csv. Lets see the complete functionality using --help option.::

    $ nsecli --help
    Usage: nsecli history [OPTIONS]

    Options:

      -S, --symbol TEXT          Security code

      -s, --start TEXT           Start date in yyyy-mm-dd format

      -e, --end TEXT             End date in yyyy-mm-dd format
      
      -o, --file TEXT            Output file name

      --series TEXT              Default series - EQ

      --index / --no-index       --index if security is index else --no-index
                                    
      --help                     Show this message and exit.


Similar to stocks you can get Index data, just by adding --index flag - ::

    $ nsecli history --symbol "NIFTY 100" -s 2017-07-01 -e 2017-07-27 -o output.csv --index


.. disqus::


                                
Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`



