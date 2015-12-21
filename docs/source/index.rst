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

>> from nsepy import get_history
>> from datetime import date
>> start = date(2015,1,1)
>> end = date(2015,1,31)
>> data = get_history(symbol="SBIN", start=start, end=end)
>> data[['Close']].plot()

Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

