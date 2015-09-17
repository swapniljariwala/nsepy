# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 09:07:27 2015

@author: swapnil jariwala
"""
#import numpy as np
import requests as req
import datetime
from bs4 import BeautifulSoup
from io import StringIO, BytesIO
NSE_URL = 'http://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?symbol=sbin&segmentLink=3&symbolCount=1&series=EQ&dateRange=+&fromDate=01-08-2015&toDate=30-09-2015&dataType=PRICEVOLUMEDELIVERABLE'
NSE_CSV = 'http://www.nseindia.com/content/equities/scripvol/datafiles/'
NSE_SYMBOL_COUNT_URL = 'http://www.nseindia.com/marketinfo/sym_map/symbolCount.jsp?symbol='
NSE_HTML_DATA_URL = 'http://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp' #symbol=SBIN&segmentLink=3&symbolCount=1&series=EQ&dateRange=1month&fromDate=&toDate=&dataType=PRICEVOLUMEDELIVERABLE'
NSE_HTML_DATA_URL_NEXT = 'http://www.nseindia.com/products/dynaContent/equities/equities/histscrip.jsp' #symbolCode=238&symbol=SBIN&symbol=SBIN&segmentLink=3&symbolCount=1&series=EQ&dateRange=1month&fromDate=&toDate=&dataType=PRICEVOLUMEDELIVERABLE'
EQ_DAILY_PRICE_LIST = 'http://www.nseindia.com/content/historical/EQUITIES/2015/SEP/cm%sbhav.csv.zip'


def __get_archive_data_raw(stock, start, end):
    url = NSE_CSV + date_to_str(start) + "-TO-" + date_to_str(end) + stock + "EQN.csv"
    resp = req.get(url)
    #print resp.request.url
    if resp.status_code == 404:
        raise ValueError('NSE denied data, try after sometime\n' + resp.request.url)
    return resp.text

def __get_html_data_raw(symbol, period = '+', start = '', end = '', proxies = {}):
    base = NSE_HTML_DATA_URL
    url = base + \
            '?symbol=%s&segmentLink=3&symbolCount=%s&series=EQ&dateRange=%s\
            &fromDate=%s&toDate=%s&dataType=PRICEVOLUMEDELIVERABLE'%(symbol,
            __get_symbol_count(symbol, proxies), period, start, end)
    resp = req.get(url,  proxies = proxies)
    if resp.status_code == 200:
        return resp.text
    else:
        return ''

def __get_symbol_count(symbol, proxies = {}):
    url = NSE_SYMBOL_COUNT_URL + symbol
    resp = req.get(url, proxies = proxies)
    return resp.text.replace('\n','')

def get_price_history_csv(fp, stock, period = '+', start = '', end = '', proxies = {}):
    text = __get_html_data_raw(symbol = stock, period = period, 
                               start = start, end = end, proxies = proxies)
    soup = BeautifulSoup(text, 'html.parser')
    for td in soup.find_all(name = 'tr'):
        if td.get_text().find('Symbol') >= 0:
            continue
        for t in td.get_text().split('\n'):
            if t:
                fp.write(t.replace(',','') + ',')
        fp.write('\n')

def get_price_history_raw(stock, period = '+', start = '', end = '', 
                          proxies = {}):
    import numpy as np
    cell_cnt = 0
    row_cnt = 0
    
    DATE = 3
    PREV_CLOSE = 4
    OPEN_PRICE = 5
    HIGH_PRICE = 6
    LOW_PRICE = 7
    LAST_PRICE = 8
    CLOSE_PRICE = 9
    VWAP = 10
    TOTAL_Q =  11
    TURNOVER = 12
    TRADES = 13
    DELIVERABLE_Q = 14
    PERC_DELIVERABLE = 15
    
    text = __get_html_data_raw(symbol = stock, period = period, 
                               start = start, end = end, proxies = proxies)
    soup = BeautifulSoup(text, 'html.parser')
    table_rows = soup.find_all(name = 'tr')
    arr_len = len(table_rows) - 1

    dates = np.array([0] * arr_len, dtype='datetime64[D]')    
    prev_close = np.zeros(arr_len)
    open_price = np.zeros(arr_len)
    high_price = np.zeros(arr_len)
    low_price  = np.zeros(arr_len)
    last_price = np.zeros(arr_len)
    close_price = np.zeros(arr_len)
    vwap = np.zeros(arr_len)
    total_q = np.zeros(arr_len)
    turnover = np.zeros(arr_len)
    trades = np.zeros(arr_len)
    deliverable_q = np.zeros(arr_len)
    perc_deliverable = np.zeros(arr_len)
    
    for row in table_rows:
        if row.get_text().find('Symbol') >= 0:
            continue        
        for cell in row.get_text().split('\n'):
            if cell_cnt == DATE:
                dates[row_cnt] =  str_to_date(cell)
            if cell_cnt == PREV_CLOSE:
                prev_close[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == OPEN_PRICE:
                open_price[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == HIGH_PRICE:
                high_price[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == LOW_PRICE:
                low_price[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == LAST_PRICE:
                last_price[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == CLOSE_PRICE:
                close_price[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == VWAP:
                vwap[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == TOTAL_Q:
                total_q[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == TURNOVER:
                turnover[row_cnt] = float(cell.replace(',','')) * 100000
            if cell_cnt == TRADES:
                trades[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == DELIVERABLE_Q:
                deliverable_q[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == PERC_DELIVERABLE:
                perc_deliverable[row_cnt] = float(cell.replace(',',''))
            cell_cnt += 1
        cell_cnt = 0
        row_cnt += 1
    return (dates, prev_close, open_price, high_price,
            low_price, last_price, close_price,
            vwap, total_q, turnover, trades,
            deliverable_q, perc_deliverable)

def get_price_history(stock, period = '+', start = '', end = '', 
                          proxies = {}):
    import numpy as np
    import pandas as pd
    cell_cnt = 0
    row_cnt = 0
    
    DATE = 3
    PREV_CLOSE = 4
    OPEN_PRICE = 5
    HIGH_PRICE = 6
    LOW_PRICE = 7
    LAST_PRICE = 8
    CLOSE_PRICE = 9
    VWAP = 10
    TOTAL_Q =  11
    TURNOVER = 12
    TRADES = 13
    DELIVERABLE_Q = 14
    PERC_DELIVERABLE = 15
    
    text = __get_html_data_raw(symbol = stock, period = period, 
                               start = start, end = end, proxies = proxies)
    soup = BeautifulSoup(text, 'html.parser')
    table_rows = soup.find_all(name = 'tr')
    arr_len = len(table_rows) - 1

    dates = np.array([0] * arr_len, dtype='datetime64[D]')    
    prev_close = np.zeros(arr_len)
    open_price = np.zeros(arr_len)
    high_price = np.zeros(arr_len)
    low_price  = np.zeros(arr_len)
    last_price = np.zeros(arr_len)
    close_price = np.zeros(arr_len)
    vwap = np.zeros(arr_len)
    total_q = np.zeros(arr_len)
    turnover = np.zeros(arr_len)
    trades = np.zeros(arr_len)
    deliverable_q = np.zeros(arr_len)
    perc_deliverable = np.zeros(arr_len)
    
    
    for row in table_rows:
        if row.get_text().find('Symbol') >= 0:
            continue        
        for cell in row.get_text().split('\n'):
            if cell_cnt == DATE:
                dates[row_cnt] =  str_to_date(cell)
            if cell_cnt == PREV_CLOSE:
                prev_close[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == OPEN_PRICE:
                open_price[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == HIGH_PRICE:
                high_price[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == LOW_PRICE:
                low_price[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == LAST_PRICE:
                last_price[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == CLOSE_PRICE:
                close_price[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == VWAP:
                vwap[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == TOTAL_Q:
                total_q[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == TURNOVER:
                turnover[row_cnt] = float(cell.replace(',','')) * 100000.0
            if cell_cnt == TRADES:
                trades[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == DELIVERABLE_Q:
                deliverable_q[row_cnt] = float(cell.replace(',',''))
            if cell_cnt == PERC_DELIVERABLE:
                perc_deliverable[row_cnt] = float(cell.replace(',','')) / 100.0
            cell_cnt += 1
        cell_cnt = 0
        row_cnt += 1
        
    df = pd.DataFrame(prev_close)
    df.columns = ['prev_close']
    df['open_price'] = open_price
    df['high_price'] = high_price
    df['low_price'] = low_price
    df['last_price'] = last_price
    df['close_price'] = close_price
    df['vwap'] = vwap
    df['total_q'] = total_q
    df['turnover'] = turnover
    df['trades'] = trades
    df['deliverable_q'] = deliverable_q
    df['perc_deliverable'] = perc_deliverable
    df.index = dates
    return df
    
def stock_history(stock, start, end, output):
    text = __get_archive_data_raw(stock, start, end)
    with open(output, 'w') as f:
        f.write(text)

def get_price_list(dt, proxies = {}):
    dt_text = date_to_str(dt, style = 'ddMMMyyyy').upper()
    url = EQ_DAILY_PRICE_LIST%dt_text
    resp = req.get(url, stream = True, proxies = proxies)
    return pd.read_csv(
                        StringIO(
                        unicode(__raw_zip_data_to_str(resp.content)
                        )
                        )
                        )

def __raw_zip_data_to_str(data):
    fp = BytesIO(data)
    import zipfile
    zipfile = zipfile.ZipFile(fp)
    name = zipfile.filelist[0].filename
    return zipfile.read(name)
        
def date_to_str(d, style = 'dd-mm-yyyy'):
    if style == 'dd-mm-yyyy':
        return str(d.day).zfill(2) + '-' + str(d.month).zfill(2) + '-' + str(d.year).zfill(2)
    elif style == 'ddMMMyyyy':
        lookup = dict((k,v) for k,v in enumerate(calendar.month_abbr))
        return str(d.day).zfill(2) + lookup[d.month] + str(d.year)

def str_to_date(d):
    k = d.split('-')
    import calendar
    import numpy as np
    lookup = dict((v,k) for k,v in enumerate(calendar.month_abbr))
    return np.datetime64(k[2] + '-' + str(lookup[k[1]]).zfill(2) + '-' + k[0])
        
if __name__ == "__main__":

    d = get_price_list(date(2015, 9, 16), proxies = {'http':'proxy1.wipro.com;8080'})
    print (d)
