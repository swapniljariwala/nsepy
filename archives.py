# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 09:07:27 2015

@author: swapnil jariwala
"""
#import numpy as np
import requests as req
import datetime
from bs4 import BeautifulSoup
NSE_URL = 'http://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?symbol=sbin&segmentLink=3&symbolCount=1&series=EQ&dateRange=+&fromDate=01-08-2015&toDate=30-09-2015&dataType=PRICEVOLUMEDELIVERABLE'
NSE_CSV = 'http://www.nseindia.com/content/equities/scripvol/datafiles/'
NSE_SYMBOL_COUNT_URL = 'http://www.nseindia.com/marketinfo/sym_map/symbolCount.jsp?symbol='
NSE_HTML_DATA_URL = 'http://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp' #symbol=SBIN&segmentLink=3&symbolCount=1&series=EQ&dateRange=1month&fromDate=&toDate=&dataType=PRICEVOLUMEDELIVERABLE'
NSE_HTML_DATA_URL_NEXT = 'http://www.nseindia.com/products/dynaContent/equities/equities/histscrip.jsp' #symbolCode=238&symbol=SBIN&symbol=SBIN&segmentLink=3&symbolCount=1&series=EQ&dateRange=1month&fromDate=&toDate=&dataType=PRICEVOLUMEDELIVERABLE'



def __get_archive_data_raw(stock, start, end):
    url = NSE_CSV + date_to_str(start) + "-TO-" + date_to_str(end) + stock + "EQN.csv"
    resp = req.get(url)
    #print resp.request.url
    if resp.status_code == 404:
        raise ValueError, 'NSE denied data, try after sometime\n' + resp.request.url
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
    text = __get_html_data_raw(symbol = stock, period = period, 
                               start = start, end = end, proxies = proxies)
    soup = BeautifulSoup(text, 'html.parser')
    for td in soup.find_all(name = 'tr'):
        if td.get_text().find('Symbol') >= 0:
            continue
        for t in td.get_text().split('\n'):
            if t:
                try:
                    print float(t.replace(',',''))
                except ValueError:
                    print 'value'
def stock_history(stock, start, end, output):
    text = __get_archive_data_raw(stock, start, end)
    with open(output, 'w') as f:
        f.write(text)
    
def date_to_str(d):    
    return str(d.day).zfill(2) + '-' + str(d.month).zfill(2) + '-' + str(d.year).zfill(2)

if __name__ == "__main__":
    get_price_history_raw(stock = 'JINDALSTEL',start = '01-01-2014', end = '10-01-2014', 
                          proxies = {'http':'proxy1.wipro.com:8080'})