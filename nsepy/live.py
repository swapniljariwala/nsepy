# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 21:51:41 2015

@author: SW274998
"""
from nsepy.commons import *
import ast
import json
from nsepy.liveurls import quote_eq_url, quote_derivative_url, option_chain_url



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
        res = quote_derivative_url(symbol, instrument, expiry_str, option_type, strike)

    res = quote_eq_url(symbol, series)

    return json.loads(res.text)['data'][0]
