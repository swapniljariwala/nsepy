# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 19:00:45 2015

@author: SW274998
"""

from nsepy.commons import URLFetch
from requests import Session
from functools import partial
from nsepy.constants import symbol_count, symbol_list

headers = {'Accept' : '*/*',
          'Accept-Language' : 'en-US,en;q=0.5',
          'Host': 'nseindia.com',
          'Referer': 'http://nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=INFY&illiquid=0',
          'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
          'X-Requested-With': 'XMLHttpRequest'
          }
get_quote = URLFetch(url = 'http://nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp',
                     headers=headers)

