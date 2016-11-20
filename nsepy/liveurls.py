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

"""
1. Stock symbol
2. Series eg. EQ, N1 ...
"""
quote_eq_url = URLFetch(url='https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxGetQuoteJSON.jsp?symbol=%s&series=%s',
                     headers=headers)

"""
1. Underlying security (stock symbol or index name)
2. instrument (FUTSTK, OPTSTK, FUTIDX, OPTIDX)
3. expiry (ddMMMyyyy)
4. type (CE/PE for options, - for futures
5. strike (strike price upto two decimal places
"""
quote_derivative_url = URLFetch(url='https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxFOGetQuoteJSON.jsp?underlying=%s&instrument=%s&expiry=%s&type=%s&strike=%s', headers=headers)

"""
1. Underlying symbol
2. instrument (FUTSTK, OPTSTK, FUTIDX, OPTIDX)
3. expiry date (ddMMMyyyy) where dd is not padded with zero when date is single digit
"""
option_chain_url = URLFetch(url='https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?segmentLink=17&symbol=%s&instrument=%s&ate=%s')
