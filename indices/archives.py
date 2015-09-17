import requests as req
import datetime
try:
    import numpy as np
    import pandas as pd
except:
    pass

from bs4 import BeautifulSoup
from io import StringIO, BytesIO

from nsepy.archives import date_to_str

PRICE_HISTORY = 'http://www.nseindia.com/content/indices/histdata/%s%s-%s.csv'
PE_HISTORY = 'http://www.nseindia.com/content/indices/histdata/%sall%s-TO-%s.csv'


def get_price_history(index, start, end, proxies = {}):

    if type(start) == type(datetime.date(2000,1,1)):
        start = date_to_str(start)
    if type(end) == type(datetime.date(2000,1,1)):
        end = date_to_str(end)
    url = PRICE_HISTORY%(index.upper().replace(' ','%20'), start, end)
    resp = req.get(url = url, proxies = proxies)
    df = pd.read_csv(StringIO(unicode(resp.text))).set_index(['Date'])
    df['Turnover (Rs. Cr)'] = df['Turnover (Rs. Cr)'] 
    return df
    
def get_index_pe(index, start, end, proxies = {}):
    if type(start) == type(datetime.date(2000,1,1)):
        start = date_to_str(start)
    if type(end) == type(datetime.date(2000,1,1)):
        end = date_to_str(end)
    url = PE_HISTORY%(index.upper().replace(' ','%20'), start, end)
    resp = req.get(url = url, proxies = proxies)
    df = pd.read_csv(StringIO(unicode(resp.text))).set_index(['Date'])
    del df['Unnamed: 4']
    return df
    