# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 21:51:41 2015

@author: SW274998
"""
from nsepy.commons import *
import ast
import json
from nsepy.liveurls import quote_eq_url, quote_derivative_url, option_chain_url


eq_quote_referer = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol={}&illiquid=0&smeFlag=0&itpFlag=0"
derivative_quote_referer = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuoteFO.jsp?underlying={}&instrument={}&expiry={}&type={}&strike={}"

def get_quote(symbol, series='EQ', instrument=None, expiry=None, option_type=None, strike=None):
    """
    1. Underlying security (stock symbol or index name)
    2. instrument (FUTSTK, OPTSTK, FUTIDX, OPTIDX)
    3. expiry (ddMMMyyyy)
    4. type (CE/PE for options, - for futures
    5. strike (strike price upto two decimal places
    """

    if instrument:
        expiry_str = "%02d%s%d"%(expiry.day, months[expiry.month][0:3].upper(), expiry.year)
        quote_derivative_url.session.headers.update({'Referer': eq_quote_referer.format(symbol)})
        res = quote_derivative_url(symbol, instrument, expiry_str, option_type, "{:0.2f}".format(strike))
    else:
        quote_eq_url.session.headers.update({'Referer': eq_quote_referer.format(symbol)})
        res = quote_eq_url(symbol, series)

    d =  json.loads(res.text)['data'][0]
    res = {}
    for k in d.keys():
        v = d[k]
        try:
            v_ = None
            if v.find('.') > 0:
                v_ = float(v.strip().replace(',', ''))
            else:
                v_ = int(v.strip().replace(',', ''))
        except:
            v_ = v
        res[k] = v_
    return res
