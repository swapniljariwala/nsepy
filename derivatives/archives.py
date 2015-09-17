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

PRICE_LIST_URL = 'http://www.nseindia.com/content/historical/DERIVATIVES/%s/%s/fo%sbhav.csv.zip'

def get_price_list(dt , proxies = {}):
    dt_str = date_to_str(dt, style = 'ddMMMyyyy')
    yy = dt_str[5:9]
    mm = dt_str[2:5].upper()
    url = PRICE_LIST_URL%(yy, mm, dt_str.upper())
    print url
    resp = req.get(url = url, proxies = proxies)
    return resp