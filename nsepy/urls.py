# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:35:13 2015

@author: SW274998
"""

from nsepy.commons import URLFetch
from requests import Session
from functools import partial

session = Session()
proxy = {'http':'proxy1.wipro.com:8080'}
NSE_SYMBOL_COUNT_URL = 'http://www.nseindia.com/marketinfo/sym_map/symbolCount.jsp'

symbol_count_url = URLFetch(url='http://www.nseindia.com/marketinfo/sym_map/symbolCount.jsp',
                            session=session)
def get_symbol_count(symbol):
    return symbol_count_url(symbol=symbol).text.lstrip().rstrip()
    
#symbol=SBIN&segmentLink=3&symbolCount=1&series=EQ&dateRange=1month&fromDate=&toDate=&dataType=PRICEVOLUMEDELIVERABLE'
equity_history_url_full = URLFetch(url='http://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp',
                              session=session)
                              

equity_history_url = partial(equity_history_url_full,
                             dataType='PRICEVOLUMEDELIVERABLE',
                             segmentLink=3)
