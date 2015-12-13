# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:33:20 2015

@author: SW274998
"""
from nsepy.archives import get_price_history, get_price_list, str_to_date
from nsepy.archives import ThreadReturns, get_price_history_small
from nsepy.archives import __get_symbol_count
from nsepy import derivatives as ddt, indices


import datetime
from datetime import date
import time

from multiprocessing.pool import ThreadPool
import threading

import pandas as pd
import numpy as np
import matplotlib as plt
from bs4 import BeautifulSoup


from matplotlib.pyplot import subplots, draw
from matplotlib.finance import candlestick

    
    
    
if __name__ == '__main__':     
    proxies = {'http':'proxy1.wipro.com:8080'}
    
    s = time.clock()
    kwarg1 = {'index' : 'CNX Nifty', 'start' : date(2015,9,1), 'end' : date(2015,9,24), 'proxies' : proxies}
    kwarg2 = {'stock' : 'WIPRO', 'start' : date(2015,9,1), 'end' : date(2015,9,24), 'proxies' : proxies}
    t1 = ThreadReturns(target = indices.archives.get_price_history,
                       kwargs = kwarg1)
    t2 = ThreadReturns(target = get_price_history,
                       kwargs = kwarg2)
    t3 = ThreadReturns(target = indices.archives.get_pe_history, kwargs = kwarg1)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    e = time.clock()
    print (e - s)
    ind = indices.archives.get_price_history(**kwarg1)
    #lt = get_price_history(**kwarg2)    
    
    ind = t1.result
    lt = t2.result
    pe = t3.result
    '''
    lt['index'] = ltni.index
    lt.drop_duplicates(subset='index', take_last=True, inplace=True)
    del lt['index']
    '''
    lt['NIFTY'] = ind['Close']
    lt['P/E'] = pe['P/E']
    data = lt
    ax = subplots()
    candlestick(ax,data['Open'],data['High'],data['Low'],data['Close'])
    
        
   
   
    