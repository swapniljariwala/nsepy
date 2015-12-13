# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:25:54 2015

@author: Swapnil Jariwala
"""

from nsepy.urls import *
import six
from nsepy.commons import *
from nsepy.constants import *
from datetime import date, timedelta
from bs4 import BeautifulSoup
import pandas as pd

dd_mmm_yyyy = StrDate.default_format(format="%d-%b-%Y")
EQUITY_SCHEMA = [str, str,
          dd_mmm_yyyy,
          float, float, float, float,
          float, float, float, int, float,
          int, int, float]
EQUITY_HEADERS = ["Symbol", "Series", "Date", "Prev Close", 
          "Open", "High", "Low","Last", "Close", "VWAP",
          "Volume", "Turnover", "Trades", "Deliverable Volume",
          "%Deliverble"]

FUTURES_SCHEMA = [str, dd_mmm_yyyy, dd_mmm_yyyy,
                  float, float, float, float,
                  float, float, int, float,
                  int, int, float]

FUTURES_HEADERS = ['Symbol', 'Date', 'Expiry',
                   'Open', 'High', 'Low', 'Close',
                   'Last', 'Settle Price', 'Number of Contracts', 'Turnover',
                   'Open Interest', 'Change in OI', 'Underlying']

OPTION_SCHEMA = [str, dd_mmm_yyyy, dd_mmm_yyyy, str, float,
                 float, float, float, float,
                 float, float, int, float,
                 float, int, int, float]
               

OPTION_HEADERS = ['Symbol', 'Date', 'Expiry', 'Option Type', 'Strike Price',
                  'Open', 'High', 'Low', 'Close',
                  'Last', 'Settle Price', 'Number of Contracts', 'Turnover',
                  'Premium Turnover', 'Open Interest', 'Change in OI', 'Underlying']

INDEX_SCHEMA = [dd_mmm_yyyy,
                float, float, float, float,
                int, float]
INDEX_HEADERS = ['Date',
                 'Open', 'High', 'Low', 'Close',
                 'Volume', 'Turnover']
VIX_INDEX_SCHEMA = [dd_mmm_yyyy,
                    float, float, float, float, 
                    float, float, float]
VIX_INDEX_HEADERS = ['Date',
                     'Open', 'High', 'Low', 'Close',
                     'Previous', 'Change', '%Change']

"""
    symbol = "SBIN" (stock name, index name and VIX)
    start = date(yyyy,mm,dd)
    end = date(yyyy,mm,dd)
    index = True, False (True even for VIX)
    ---------------
    futures = True, False
    option_type = "CE", "PE", "CA", "PA"
    strike_price = integer number
    expiry_date = date(yyyy,mm,dd)

"""
def get_history(**kwargs):
    start = kwargs['start']
    end = kwargs['end']
    if (end - start) > timedelta(130):
        kwargs1 = dict(kwargs)
        kwargs2 = dict(kwargs)
        kwargs1['end'] = start + timedelta(130)
        kwargs2['start'] = kwargs1['end'] + timedelta(1)
        t1 = ThreadReturns(target=get_history, kwargs=kwargs1)
        t2 = ThreadReturns(target=get_history, kwargs=kwargs2)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        return pd.concat((t1.result, t2.result))
    else:
        return get_history_quanta(**kwargs) 
        
    
    
def get_history_quanta(**kwargs):
    url, params, schema, headers = validate_params(**kwargs)
    df = url_to_df(url=url,
                   params=params,
                   schema=schema,
                   headers=headers)
    return df


def url_to_df(url, params, schema, headers):
    resp = url(**params)
    bs = BeautifulSoup(resp.text)
    tp = ParseTables(soup=bs,
                     schema=schema,
                     headers=headers, index="Date")
    return tp.get_df()
                    
"""
    symbol = "SBIN" (stock name, index name and VIX)
    start = date(yyyy,mm,dd)
    end = date(yyyy,mm,dd)
    index = True, False (True even for VIX)
    ---------------
    futures = True, False
    option_type = "CE", "PE", "CA", "PA"
    strike_price = integer number
    expiry_date = date(yyyy,mm,dd)

    
"""
def validate_params(symbol, start, end, index=False, futures=False, option_type="",
                    expiry_date = None, strike_price="", series='EQ'):
    params = {}
    
    
    if (futures and not option_type) or (not futures and option_type): #EXOR
        params['symbol'] = symbol
        params['dateRange'] = ''
        params['optionType'] = 'select'
        params['strikePrice'] = ''
        params['fromDate'] = start.strftime('%d-%b-%Y')
        params['toDate'] = end.strftime('%d-%b-%Y')
        url = derivative_history_url

       
        params['expiryDate'] = expiry_date.strftime("%d-%m-%Y")
        option_type = option_type.upper()
        if option_type in ("CE", "PE", "CA", "PA"):
            if not isinstance(strike_price,int):
                raise ValueError("strike_price argument missing or not of type int")
            #option specific
            if index: params['instrumentType'] = 'OPTIDX'
            else: params['instrumentType'] = 'OPTSTK'
            params['strikePrice'] = strike_price
            params['optionType'] = option_type
            schema = OPTION_SCHEMA
            headers = OPTION_HEADERS
        elif option_type: 
            #this means that there's an invalid value in option_type
            raise ValueError("Invalid value in option_type, valid values-'CE' or 'PE' or 'CA' or 'CE'")
        else:
            # its a futures request
            if index:
                if symbol=='INDIAVIX': params['instrumentType'] = 'FUTIVX'
                else: params['instrumentType'] = 'FUTIDX'
            else: params['instrumentType'] = 'FUTSTK'            
            schema = FUTURES_SCHEMA
            headers = FUTURES_HEADERS
    elif futures and option_type: 
        raise ValueError("select either futures='True' or option_type='CE' or 'PE' not both")
    else: # its a normal request
        
        if index:
            if symbol=='INDIAVIX':
                params['fromDate'] = start.strftime('%d-%b-%Y')
                params['toDate'] = end.strftime('%d-%b-%Y')
                url = index_vix_history_url
                schema = VIX_INDEX_SCHEMA
                headers = VIX_INDEX_HEADERS
            else: 
                params['indexType'] = symbol
                params['fromDate'] = start.strftime('%d-%m-%Y')
                params['toDate'] = end.strftime('%d-%m-%Y')
                url = index_history_url
                schema = INDEX_SCHEMA
                headers = INDEX_HEADERS
        else:
            params['symbol'] = symbol
            params['series'] = series
            params['symbolCount'] = get_symbol_count(symbol)
            url = equity_history_url
            schema = EQUITY_SCHEMA
            headers = EQUITY_HEADERS
    
    return url, params, schema, headers
            
        
