# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:35:13 2015

@author: SW274998
"""

from nsepy.commons import URLFetch
from requests import Session
from functools import partial
from nsepy.constants import symbol_count, symbol_list


session = Session()
# headers = {
    # 'Host': 'www1.nseindia.com',
    # 'Referer': 'https://www1.nseindia.com/products/content/equities/equities/eq_security.htm'}

headers = {'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate, sdch, br',
           'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6',
           'Connection': 'keep-alive',
           'Host': 'www1.nseindia.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest'}

URLFetchSession = partial(URLFetch, session=session,
                          headers=headers)

NSE_SYMBOL_COUNT_URL = 'http://www1.nseindia.com/marketinfo/sym_map/symbolCount.jsp'


"""
---------------------------------EQUITY--------------------------------------
"""
symbol_count_url = URLFetchSession(
    url='http://www1.nseindia.com/marketinfo/sym_map/symbolCount.jsp')


def get_symbol_count(symbol):
    try:
        return symbol_count[symbol]
    except:
        cnt = symbol_count_url(symbol=symbol).text.lstrip().rstrip()
        symbol_count[symbol] = cnt
        return cnt


"""
#symbol=SBIN&segmentLink=3&symbolCount=1&series=EQ&dateRange=1month&fromDate=&toDate=&dataType=PRICEVOLUMEDELIVERABLE'
"""
equity_history_url_full = URLFetchSession(
    url='http://www1.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp')

"""
symbol="SBIN"
symbolCount=get_symbol_count(SBIN)
series="EQ"
fromDate="dd-mm-yyyy"
toDate="dd-mm-yyyy"
dd = equity_history_url(symbol='SBIN', series="EQ", fromDate="01-01-2017", toDate="01-01-2017")
"""
equity_history_url = partial(equity_history_url_full,
                             dataType='PRICEVOLUMEDELIVERABLE',
                             segmentLink=3, dateRange="")

"""
1. YYYY
2. MMM
3. ddMMMyyyy
"""
price_list_url = URLFetchSession(
    url='https://www1.nseindia.com/content/historical/EQUITIES/%s/%s/cm%sbhav.csv.zip')

"""
1. ddmmyyyy
"""
daily_volatility_url = URLFetchSession(
    url='http://www1.nseindia.com/archives/nsccl/volt/CMVOLT_%s.CSV')

"""
1. ddmmyyyy
"""
daily_deliverypositions_url = URLFetchSession(
    url='https://www1.nseindia.com/archives/equities/mto/MTO_%s.DAT')


"""
1. ddmmyy
"""
pr_price_list_zipped_url = URLFetchSession(
    url='http://www1.nseindia.com/archives/equities/bhavcopy/pr/PR%s.zip')


"""
--------------------------INDICES---------------------------------------
"""
"""
1. indexType=index name
2. fromDate string dd-mm-yyyy
3. toDate string dd-mm-yyyy
"""
index_history_url = URLFetchSession(
    url='http://www1.nseindia.com/products/dynaContent/equities/indices/historicalindices.jsp')

"""
1. ddmmyyyy
"""
index_daily_snapshot_url = URLFetchSession(
    url='https://archives.nseindia.com/content/indices/ind_close_all_%s.csv')

"""
indexName=NIFTY%2050&fromDate=02-11-2015&toDate=19-11-2015&yield1=undefined&yield2=undefined&yield3=undefined&yield4=all
indexName = Index name
fromDate = from date dd-mm-yyyy
toDate = to Date dd-mm-yyyy
"""
index_pe_history_url = partial(
    URLFetchSession(
        url='http://www1.nseindia.com/products/dynaContent/equities/indices/historical_pepb.jsp?'),
    yield1="undefined",
    yield2="undefined",
    yield3="undefined",
    yield4="all")
"""
http://www1.nseindia.com/products/dynaContent/equities/indices/hist_vix_data.jsp?&fromDate=01-Nov-2015&toDate=19-Nov-2015
fromDate = 'dd-Mmm-yyyy'
toDate = 'dd-Mmm-yyyy'
"""
index_vix_history_url = URLFetchSession(
    url='http://www1.nseindia.com/products/dynaContent/equities/indices/hist_vix_data.jsp')

equity_symbol_list_url = URLFetchSession(
    url='https://www1.nseindia.com/content/equities/EQUITY_L.csv')

index_constituents_url = URLFetchSession(
    "https://www1.nseindia.com/content/indices/ind_%slist.csv")

"""
--------------------------DERIVATIVES---------------------------------------
"""
derivative_expiry_dates_url = URLFetchSession(
    url='http://www1.nseindia.com/products/resources/js/foExp.js')

"""
instrumentType=FUTIDX
symbol=NIFTY
expiryDate=26-11-2015
optionType=select
strikePrice=
dateRange=15days
fromDate= 01-Nov-2015
toDate=19-Nov-2015
segmentLink=9&
symbolCount=
"""
derivative_history_url = partial(
    URLFetchSession(
        url='http://www1.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?',
        headers = {**headers, **{'Referer': 'https://www1.nseindia.com/products/content/derivatives/equities/historical_fo.htm'}}
        #headers = (lambda a,b: a.update(b) or a)(headers.copy(),{'Referer': 'https://www1.nseindia.com/products/content/derivatives/equities/historical_fo.htm'})
        ),
    segmentLink=9,
    symbolCount='')
"""
http://www1.nseindia.com/content/historical/DERIVATIVES/2015/NOV/fo18NOV2015bhav.csv.zip
1.year yyyy
2.Month MMM
3.date ddMMMyyyy

"""
derivative_price_list_url = URLFetchSession(
    url="http://www1.nseindia.com/content/historical/DERIVATIVES/%s/%s/fo%sbhav.csv.zip")


"""
--------------------------CURRENCY---------------------------------------
"""
"""
fromDate dd-mm-yyyy (from date)
toDate dd-mm-yyyy (to date)
"""
rbi_rate_history_url = URLFetchSession(
    "https://www1.nseindia.com/products/dynaContent/derivatives/currency/fxRbiRateHist.jsp")
