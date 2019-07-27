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
import six
import inspect
import io
import pdb

dd_mmm_yyyy = StrDate.default_format(format="%d-%b-%Y")
dd_mm_yyyy = StrDate.default_format(format="%d-%m-%Y")
EQUITY_SCHEMA = [str, str,
                 dd_mmm_yyyy,
                 float, float, float, float,
                 float, float, float, int, float,
                 int, int, float]
EQUITY_HEADERS = ["Symbol", "Series", "Date", "Prev Close",
                  "Open", "High", "Low", "Last", "Close", "VWAP",
                  "Volume", "Turnover", "Trades", "Deliverable Volume",
                  "%Deliverble"]
EQUITY_SCALING = {"Turnover": 100000,
                  "%Deliverble": 0.01}

FUTURES_SCHEMA = [str, dd_mmm_yyyy, dd_mmm_yyyy,
                  float, float, float, float,
                  float, float, int, float,
                  int, int, float]

FUTURES_HEADERS = ['Symbol', 'Date', 'Expiry',
                   'Open', 'High', 'Low', 'Close',
                   'Last', 'Settle Price', 'Number of Contracts', 'Turnover',
                   'Open Interest', 'Change in OI', 'Underlying']
FUTURES_SCALING = {"Turnover": 100000}

OPTION_SCHEMA = [str, dd_mmm_yyyy, dd_mmm_yyyy, str, float,
                 float, float, float, float,
                 float, float, int, float,
                 float, int, int, float]
OPTION_HEADERS = ['Symbol', 'Date', 'Expiry', 'Option Type', 'Strike Price',
                  'Open', 'High', 'Low', 'Close',
                  'Last', 'Settle Price', 'Number of Contracts', 'Turnover',
                  'Premium Turnover', 'Open Interest', 'Change in OI', 'Underlying']
OPTION_SCALING = {"Turnover": 100000,
                  "Premium Turnover": 100000}


INDEX_SCHEMA = [dd_mmm_yyyy,
                float, float, float, float,
                int, float]
INDEX_HEADERS = ['Date',
                 'Open', 'High', 'Low', 'Close',
                 'Volume', 'Turnover']
INDEX_SCALING = {'Turnover': 10000000}

VIX_INDEX_SCHEMA = [dd_mmm_yyyy,
                    float, float, float, float,
                    float, float, float]
VIX_INDEX_HEADERS = ['Date',
                     'Open', 'High', 'Low', 'Close',
                     'Previous', 'Change', '%Change']
VIX_SCALING = {'%Change': 0.01}

INDEX_PE_SCHEMA = [dd_mmm_yyyy,
                   float, float, float]
INDEX_PE_HEADERS = ['Date', 'P/E', 'P/B', 'Div Yield']

RBI_REF_RATE_SCHEMA = [dd_mmm_yyyy, float, float, float, float]
RBI_REF_RATE_HEADERS = ['Date', '1 USD', '1 GBP', '1 EURO', '100 YEN']

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


def get_history(symbol, start, end, index=False, futures=False, option_type="",
                expiry_date=None, strike_price="", series='EQ'):
    """This is the function to get the historical prices of any security (index,
        stocks, derviatives, VIX) etc.

        Args:
            symbol (str): Symbol for stock, index or any security
            start (datetime.date): start date
            end (datetime.date): end date
            index (boolean): False by default, True if its a index
            futures (boolean): False by default, True for index and stock futures
            expiry_date (datetime.date): Expiry date for derivatives, Compulsory for futures and options
            option_type (str): It takes "CE", "PE", "CA", "PA" for European and American calls and puts
            strike_price (int): Strike price, Compulsory for options
            series (str): Defaults to "EQ", but can be "BE" etc (refer NSE website for details)

        Returns:
            pandas.DataFrame : A pandas dataframe object 

        Raises:
            ValueError: 
                        1. strike_price argument missing or not of type int when options_type is provided
                        2. If there's an Invalid value in option_type, valid values-'CE' or 'PE' or 'CA' or 'CE'
                        3. If both futures='True' and option_type='CE' or 'PE'
    """
    frame = inspect.currentframe()
    args, _, _, kwargs = inspect.getargvalues(frame)
    del(kwargs['frame'])
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
    url, params, schema, headers, scaling = validate_params(**kwargs)
    df = url_to_df(url=url,
                   params=params,
                   schema=schema,
                   headers=headers, scaling=scaling)
    return df


def url_to_df(url, params, schema, headers, scaling={}):
    resp = url(**params)
    bs = BeautifulSoup(resp.text, 'lxml')
    tp = ParseTables(soup=bs,
                     schema=schema,
                     headers=headers, index="Date")
    df = tp.get_df()
    for key, val in six.iteritems(scaling):
        df[key] = val * df[key]
    return df


def validate_params(symbol, start, end, index=False, futures=False, option_type="",
                    expiry_date=None, strike_price="", series='EQ'):
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

    params = {}

    if start > end:
        raise ValueError('Please check start and end dates')

    if (futures and not option_type) or (not futures and option_type):  # EXOR
        params['symbol'] = symbol
        params['dateRange'] = ''
        params['optionType'] = 'select'
        params['strikePrice'] = ''
        params['fromDate'] = start.strftime('%d-%b-%Y')
        params['toDate'] = end.strftime('%d-%b-%Y')
        url = derivative_history_url

        try:
            params['expiryDate'] = expiry_date.strftime("%d-%m-%Y")
        except AttributeError as e:
            raise ValueError(
                'Derivative contracts must have expiry_date as datetime.date')

        option_type = option_type.upper()
        if option_type in ("CE", "PE", "CA", "PA"):
            if not isinstance(strike_price, int) and not isinstance(strike_price, float):
                raise ValueError(
                    "strike_price argument missing or not of type int or float")
            # option specific
            if index:
                params['instrumentType'] = 'OPTIDX'
            else:
                params['instrumentType'] = 'OPTSTK'
            params['strikePrice'] = strike_price
            params['optionType'] = option_type
            schema = OPTION_SCHEMA
            headers = OPTION_HEADERS
            scaling = OPTION_SCALING
        elif option_type:
            # this means that there's an invalid value in option_type
            raise ValueError(
                "Invalid value in option_type, valid values-'CE' or 'PE' or 'CA' or 'CE'")
        else:
            # its a futures request
            if index:
                if symbol == 'INDIAVIX':
                    params['instrumentType'] = 'FUTIVX'
                else:
                    params['instrumentType'] = 'FUTIDX'
            else:
                params['instrumentType'] = 'FUTSTK'
            schema = FUTURES_SCHEMA
            headers = FUTURES_HEADERS
            scaling = FUTURES_SCALING
    elif futures and option_type:
        raise ValueError(
            "select either futures='True' or option_type='CE' or 'PE' not both")
    else:  # its a normal request

        if index:
            if symbol == 'INDIAVIX':
                params['fromDate'] = start.strftime('%d-%b-%Y')
                params['toDate'] = end.strftime('%d-%b-%Y')
                url = index_vix_history_url
                schema = VIX_INDEX_SCHEMA
                headers = VIX_INDEX_HEADERS
                scaling = VIX_SCALING
            else:
                if symbol in DERIVATIVE_TO_INDEX:
                    params['indexType'] = DERIVATIVE_TO_INDEX[symbol]
                else:
                    params['indexType'] = symbol
                params['fromDate'] = start.strftime('%d-%m-%Y')
                params['toDate'] = end.strftime('%d-%m-%Y')
                url = index_history_url
                schema = INDEX_SCHEMA
                headers = INDEX_HEADERS
                scaling = INDEX_SCALING
        else:
            params['symbol'] = symbol
            params['series'] = series
            params['symbolCount'] = get_symbol_count(symbol)
            params['fromDate'] = start.strftime('%d-%m-%Y')
            params['toDate'] = end.strftime('%d-%m-%Y')
            url = equity_history_url
            schema = EQUITY_SCHEMA
            headers = EQUITY_HEADERS
            scaling = EQUITY_SCALING

    return url, params, schema, headers, scaling


def get_index_pe_history(symbol, start, end):
    frame = inspect.currentframe()
    args, _, _, kwargs = inspect.getargvalues(frame)
    del(kwargs['frame'])
    start = kwargs['start']
    end = kwargs['end']
    if (end - start) > timedelta(130):
        kwargs1 = dict(kwargs)
        kwargs2 = dict(kwargs)
        kwargs1['end'] = start + timedelta(130)
        kwargs2['start'] = kwargs1['end'] + timedelta(1)
        t1 = ThreadReturns(target=get_index_pe_history, kwargs=kwargs1)
        t2 = ThreadReturns(target=get_index_pe_history, kwargs=kwargs2)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        return pd.concat((t1.result, t2.result))
    else:
        return get_index_pe_history_quanta(**kwargs)


def get_index_pe_history_quanta(symbol, start, end):
    """This function will fetch the P/E, P/B and dividend yield for a given index

        Args:
            symbol (str): Symbol for stock, index or any security
            start (datetime.date): start date
            end (datetime.date): end date

        Returns:
            pandas.DataFrame : A pandas dataframe object 
    """
    if symbol in DERIVATIVE_TO_INDEX:
        index_name = DERIVATIVE_TO_INDEX[symbol]
    else:
        index_name = symbol
    resp = index_pe_history_url(indexName=index_name,
                                fromDate=start.strftime('%d-%m-%Y'),
                                toDate=end.strftime('%d-%m-%Y'))

    bs = BeautifulSoup(resp.text, 'lxml')
    tp = ParseTables(soup=bs,
                     schema=INDEX_PE_SCHEMA,
                     headers=INDEX_PE_HEADERS, index="Date")
    df = tp.get_df()
    return df


def get_price_list(dt, series='EQ'):
    MMM = dt.strftime("%b").upper()
    yyyy = dt.strftime("%Y")

    """
    1. YYYY
    2. MMM
    3. ddMMMyyyy
    """
    res = price_list_url(yyyy, MMM, dt.strftime("%d%b%Y").upper())
    txt = unzip_str(res.content)
    fp = six.StringIO(txt)
    df = pd.read_csv(fp)
    del df['Unnamed: 13']
    return df[df['SERIES'] == series]


"""
Get Trade and Delivery Volume for each stock
"""


def get_delivery_position(dt, segment='EQ'):
    MMM = dt.strftime("%b").upper()
    yyyy = dt.strftime("%Y")

    """
    1. ddmmyyyy
    """
    res = daily_deliverypositions_url(dt.strftime("%d%m%Y").upper())
    text = res.content.decode()
    fp = six.StringIO(text)

    # The file starts with initial lines that just have text infomation
    # e.g.
    # Security Wise Delivery Position - Compulsory Rolling Settlement
    # 10,MTO,19072019,471778636,0001790
    # Trade Date <19-JUL-2019>,Settlement Type <N>

    # Skip the initial lines till we get to the actual data

    df = pd.read_csv(fp, names=["RECORD TYPE", "SR NO", "SYMBOL", "SEGMENT", "TRADE VOLUME", "TOTDELQTY", "PCT DEL TO TRADE"],
                     header=None, skiprows=4,
                     usecols=["SYMBOL", "SEGMENT", "TRADE VOLUME",
                              "TOTDELQTY", "PCT DEL TO TRADE"]
                     )
    flsegment = df['SEGMENT'] == segment
    df = df[flsegment]

    return df


"""
Get Price range for all Indices
"""


def get_indices_price_list(dt):
    res = index_daily_snapshot_url(dt.strftime("%d%m%Y"))
    df = pd.read_csv(io.StringIO(res.content.decode('utf-8')))
    df = df.rename(columns={"Index Name": "NAME",
                            "Index Date": "TIMESTAMP",
                            "Open Index Value": "OPEN",
                            "High Index Value": "HIGH",
                            "Low Index Value": "LOW",
                            "Closing Index Value": "CLOSE",
                            "Points Change": "CHANGE",
                            "Change(%)": "CHANGEPCT",
                            "Volume": "TOTTRDQTY",
                            "Turnover (Rs. Cr.)": "TOTTRDVAL",
                            "P/E": "PE",
                            "P/B": "PB",
                            "Div Yield": "DIVYIELD"})
    return df


def get_rbi_ref_history(start, end):
    frame = inspect.currentframe()
    args, _, _, kwargs = inspect.getargvalues(frame)
    del(kwargs['frame'])
    start = kwargs['start']
    end = kwargs['end']
    if (end - start) > timedelta(130):
        kwargs1 = dict(kwargs)
        kwargs2 = dict(kwargs)
        kwargs1['end'] = start + timedelta(130)
        kwargs2['start'] = kwargs1['end'] + timedelta(1)
        t1 = ThreadReturns(target=get_rbi_ref_history, kwargs=kwargs1)
        t2 = ThreadReturns(target=get_rbi_ref_history, kwargs=kwargs2)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        return pd.concat((t1.result, t2.result))
    else:
        return get_rbi_ref_history_quanta(**kwargs)


def get_rbi_ref_history_quanta(start, end):
    """
        Args:
            start (datetime.date): start date
            end (datetime.date): end date

        Returns:
            pandas.DataFrame : A pandas dataframe object 
    """
    resp = rbi_rate_history_url(fromDate=start.strftime('%d-%m-%Y'),
                                toDate=end.strftime('%d-%m-%Y'))

    bs = BeautifulSoup(resp.text, 'lxml')
    tp = ParseTables(soup=bs,
                     schema=RBI_REF_RATE_SCHEMA,
                     headers=RBI_REF_RATE_HEADERS, index="Date")
    df = tp.get_df()
    return df
