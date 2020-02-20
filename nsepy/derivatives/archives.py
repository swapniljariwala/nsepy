import requests as req
import datetime
try:
    import numpy as np
    import pandas as pd
except:
    pass

from bs4 import BeautifulSoup
from io import StringIO, BytesIO

from nsepy.archives import date_to_str, __raw_zip_data_to_str


PRICE_LIST_URL = 'http://www1.nseindia.com/content/historical/DERIVATIVES/%s/%s/fo%sbhav.csv.zip'

DERIVATIVE_ARCHIVES = 'http://www1.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?instrumentType=OPTIDX&symbol=NIFTY&expiryDate=27-07-2006&optionType=CE&strikePrice=&dateRange=week&fromDate=&toDate=&segmentLink=9&symbolCount='


def get_price_list(dt, proxies={}):
    dt_str = date_to_str(dt, style='ddMMMyyyy')
    yy = dt_str[5:9]
    mm = dt_str[2:5].upper()
    url = PRICE_LIST_URL % (yy, mm, dt_str.upper())
    resp = req.get(url=url, proxies=proxies)
    df = pd.read_csv(StringIO(
                        unicode(__raw_zip_data_to_str(resp.content))))
    del df['Unnamed: 15']
    return df


