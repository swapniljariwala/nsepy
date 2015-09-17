# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:33:20 2015

@author: SW274998
"""
from archives import get_price_history

d = get_price_history(stock = 'LT',start = '01-01-2014', end = '20-01-2014', 
                          proxies = {'http': 'proxy1.wipro.com:8080'})
d[['high_price', 'vwap', 'low_price']].plot()
