import requests as req
import datetime
try:
    import numpy as np
    import pandas as pd
except:
    pass

from bs4 import BeautifulSoup
from io import StringIO, BytesIO

from nsepy.archives import date_to_str, ThreadReturns, html_to_rows, str_to_date
from nsepy import archives
import sys
PRICE_HISTORY_CSV = 'http://www.nseindia.com/content/indices/histdata/%s%s-%s.csv'
PE_HISTORY_CSV = 'http://www.nseindia.com/content/indices/histdata/%sall%s-TO-%s.csv'
PRICE_HISTORY = 'http://www.nseindia.com/products/dynaContent/equities/indices/historicalindices.jsp?indexType=%s&fromDate=%s&toDate=%s'
PE_HISTORY = 'http://www.nseindia.com/products/dynaContent/equities/indices/historical_pepb.jsp?indexName=%s&fromDate=%s&toDate=%s&yield1=undefined&yield2=undefined&yield3=undefined&yield4=all'

def _html_to_index_df(lst):
    ''' delete top 3 rows which contain text headers'''    
    del lst[0]
    del lst[0]
    del lst[0]
    lst.pop()
    l = len(lst) 
    dates = np.empty(l, dtype = 'datetime64[D]')
    arr = np.empty([6,l])
    c_cnt = 0
    r_cnt = 0
    for r in lst:
        c_cnt = 0
        for c in r.find_all('td'):
            try:
                val = float(c.get_text().replace(',','').replace(' ',''))
            except:
                val = np.NaN
            if c_cnt == 0:
                dates[r_cnt] = str_to_date(c.text)
            elif c_cnt > 0 and c_cnt <= 6 :
                arr[c_cnt - 1][r_cnt] = val
            c_cnt += 1
        r_cnt += 1
    df = pd.DataFrame()
    
    df['Open'] = arr[0]
    df['High'] = arr[1]
    df['Low'] = arr[2]
    df['Close'] = arr[3]
    df['Shares Traded'] = arr[4]
    df['Turnover'] = arr[5]
    df.index = dates
    return df

def _html_to_pe_df(lst):
    del lst[0]
    del lst[0]
    del lst[0]
    lst.pop()
    
    l = len(lst) 
    dates = np.empty(l, dtype = 'datetime64[D]')
    arr = np.empty([3,l])
    c_cnt = 0
    r_cnt = 0
    for r in lst:
        c_cnt = 0
        for c in r.find_all('td'):
            try:
                val = float(c.get_text().replace(',','').replace(' ',''))
            except:
                val = np.NaN
            if c_cnt == 0:
                dates[r_cnt] = str_to_date(c.text)
            elif c_cnt > 0 and c_cnt <= 3 :
                arr[c_cnt - 1][r_cnt] = val
            c_cnt += 1
        r_cnt += 1
    df = pd.DataFrame()
    
    df['P/E'] = arr[0]
    df['P/B'] = arr[1]
    df['Div Yield'] = arr[2]
    
    
    df.index = dates
    return df

def _get_price_history_small(index, start, end, proxies = {}):
    
    if type(start) == type(datetime.date(2000,1,1)):
        start = date_to_str(start)
    if type(end) == type(datetime.date(2000,1,1)):
        end = date_to_str(end)
    url = PRICE_HISTORY%(index.upper().replace(' ','%20'), start, end)
    resp = req.get(url = url, proxies = proxies)
    rows = html_to_rows(resp.text)
    return _html_to_index_df(rows)
    

def get_price_history(index, start, end, proxies = {}):
    if (end - start) > datetime.timedelta(100):
        #print 'Thread:', start, end
        dt = (end - start) / 2
        end_1 = start + dt
        start_2 = end_1 + datetime.timedelta(1)
        arg1 = {'index':index, 'start': start, 'end': end_1,
                'proxies': proxies}
        arg2 = {'index':index, 'start': start_2, 'end': end,
                'proxies': proxies}
                
        t1 = ThreadReturns(target = get_price_history, 
                              kwargs = arg1)
        
        t2 = ThreadReturns(target = get_price_history, 
                              kwargs = arg2)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        return pd.concat([t1.result, t2.result])
    else:
        return _get_price_history_small(index = index, start = start,
                                        end = end, proxies = proxies)

def get_pe_history(index, start, end, proxies = {}):
    if (end - start) > datetime.timedelta(100 + 19*2):
        end_1 = start + datetime.timedelta(100 + 19*2) 
        start_2 = end_1 + datetime.timedelta(1)
        arg1 = {'index':index, 'start': start, 'end': end_1,
                'proxies': proxies}
        arg2 = {'index':index, 'start': start_2, 'end': end,
                'proxies': proxies}
                
        t1 = ThreadReturns(target = get_pe_history, 
                              kwargs = arg1)
        
        t2 = ThreadReturns(target = get_pe_history, 
                              kwargs = arg2)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        
        return pd.concat([t1.result, t2.result])
        
    else:
        return _get_pe_history_small(index = index, start = start,
                                        end = end, proxies = proxies)

def _get_pe_history_small(index, start, end, proxies = {}):
    
    if type(start) == type(datetime.date(2000,1,1)):
        start = date_to_str(start)
    if type(end) == type(datetime.date(2000,1,1)):
        end = date_to_str(end)
    url = PE_HISTORY%(index.upper().replace(' ','%20'), start, end)
    resp = req.get(url = url, proxies = proxies)
    rows = html_to_rows(resp.text)
    df = _html_to_pe_df(rows)
    
    return df
  