# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 19:00:45 2015

@author: SW274998
"""

from nsepy.commons import URLFetch
from requests import Session
from functools import partial
from nsepy.constants import symbol_count, symbol_list

headers = {'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate, sdch, br',
           'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6',
           'Connection': 'keep-alive',
           'Host': 'www1.nseindia.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest'}


"""
1. Stock symbol
2. Series eg. EQ, N1 ...
"""
quote_eq_url = URLFetch(url='https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=%s&series=%s',
                        headers=headers)
"""
1. Underlying security (stock symbol or index name)
2. instrument (FUTSTK, OPTSTK, FUTIDX, OPTIDX)
3. expiry (ddMMMyyyy)
4. type (CE/PE for options, - for futures
5. strike (strike price upto two decimal places
"""
quote_derivative_url = URLFetch(
    url='https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuoteFO.jsp?underlying=%s&instrument=%s&expiry=%s&type=%s&strike=%s', headers=headers)

"""
1. Underlying symbol
2. instrument (FUTSTK, OPTSTK, FUTIDX, OPTIDX)
3. expiry date (ddMMMyyyy) where dd is not padded with zero when date is single digit
"""
option_chain_url = URLFetch(
    url='https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?segmentLink=17&symbol=%s&instrument=%s&date=%s', headers=headers)

"""
1. symbol
2. instrument
3. date
"""

futures_chain_url = URLFetch(
    url='https://www1.nseindia.com/live_market/dynaContent/live_watch/fomwatchsymbol.jsp?key=%s&Fut_Opt=Futures', headers=headers)

"""
1. symbol
"""
holiday_list_url = URLFetch(url='https://www1.nseindia.com/global/content/market_timings_holidays/market_timings_holidays.jsp?pageName=0&dateRange=&fromDate=%s&toDate=%s&tabActive=trading&load=false',
                            headers=headers)
