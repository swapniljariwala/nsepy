# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 17:35:16 2015

@author: jerry
"""

import requests
from nsepy.archives import html_to_rows
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
FII_YEARLY_URL = 'https://www.fpi.nsdl.co.in/web/Reports/Yearwise.aspx?RptType=5'

def fii_yearly():
    resp = requests.get(FII_YEARLY_URL, verify = False, proxies = {'https':'proxy1.wipro.com:8080'})
    soup = BeautifulSoup(resp.text)
    ts = soup.find_all('table')
    trs = ts[1].find_all('tr')
    del trs[0]
    del trs[0]
    del trs[0]
    trs.pop()
    #trs.pop()
    index = []
    arr = np.empty([3,len(trs)])
    r_cnt = 0
    for r in trs:
        cs = r.find_all('td')
        c_cnt = 0
        for c in cs:
            if c_cnt == 0:
                index.append(c.text)
            if c_cnt > 0:
                arr[c_cnt - 1, r_cnt] = np.float(c.text)
            c_cnt += 1
        r_cnt += 1           
    df = pd.DataFrame()
    #df.index = index
    df['Equity'] = d[0]
    #df['Debt'] = d[1]
    #df['Total'] = d[2]
    return index, df
    
if __name__ == "__main__":
    d = fii_yearly()
    

