# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 21:51:41 2015

@author: SW274998
"""
import pdb
import dateutil.relativedelta
from nsepy.commons import *
import ast
import json
import io
from bs4 import BeautifulSoup
from nsepy.liveurls import quote_eq_url, quote_derivative_url, option_chain_url, futures_chain_url, holiday_list_url


OPTIONS_CHAIN_SCHEMA = [str, int, int, int, float, float, float, int, float, float, int,
                        float,
                        int, float, float, int, float, float, float, int, int, int, str]
OPTIONS_CHAIN_HEADERS = ["Call Chart", "Call OI", "Call Chng in OI", "Call Volume", "Call IV", "Call LTP", "Call Net Chng", "Call Bid Qty", "Call Bid Price", "Call Ask Price", "Call Ask Qty",
                         "Strike Price",
                         "Put Bid Qty", "Put Bid Price", "Put Ask Price", "Put Ask Qty", "Put Net Chng", "Put LTP", "Put IV", "Put Volume", "Put Chng in OI", "Put OI", "Put Chart"]
OPTIONS_CHAIN_INDEX = "Strike Price"

FUTURES_SCHEMA = [str, str, StrDate.default_format(
    format="%d%b%Y"), str, str, float, float, float, float, float, int, float, float]
FUTURES_HEADERS = ["Instrument", "Underlying", "Expiry Date", "Option Type", "Strike Price", "Open Price", "High Price", "Low Price", "Prev. Close", "Last Price", "Volume",
                   "Turnover", "Underlying Value"]
FUTURES_INDEX = "Expiry Date"


eq_quote_referer = "https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol={}&illiquid=0&smeFlag=0&itpFlag=0"
derivative_quote_referer = "https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuoteFO.jsp?underlying={}&instrument={}&expiry={}&type={}&strike={}"
option_chain_referer = "https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=-9999&symbol=NIFTY&symbol=BANKNIFTY&instrument=OPTIDX&date=-&segmentLink=17&segmentLink=17"


def get_quote(symbol, series='EQ', instrument=None, expiry=None, option_type=None, strike=None):
    """
    1. Underlying security (stock symbol or index name)
    2. instrument (FUTSTK, OPTSTK, FUTIDX, OPTIDX)
    3. expiry (ddMMMyyyy)
    4. type (CE/PE for options, - for futures
    5. strike (strike price upto two decimal places
    """
    if instrument:
        expiry_str = "%02d%s%d" % (
            expiry.day, months[expiry.month][0:3].upper(), expiry.year)
        quote_derivative_url.session.headers.update(
            {'Referer': eq_quote_referer.format(symbol)})
        strike_str = "{:.2f}".format(strike) if strike else ""
        res = quote_derivative_url(
            symbol, instrument, expiry_str, option_type, strike_str)
    else:
        quote_eq_url.session.headers.update(
            {'Referer': eq_quote_referer.format(symbol)})
        res = quote_eq_url(symbol, series)

    html_soup = BeautifulSoup(res.text, 'lxml')
    hresponseDiv = html_soup.find("div", {"id": "responseDiv"})
    d = json.loads(hresponseDiv.get_text())
    #d = json.loads(res.text)['data'][0]
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


def get_option_chain(symbol, instrument=None, expiry=None):

    if expiry:
        expiry_str = "%02d%s%d" % (
            expiry.day, months[expiry.month][0:3].upper(), expiry.year)
    else:
        expiry_str = "-"
    option_chain_url.session.headers.update({'Referer': option_chain_referer})
    r = option_chain_url(symbol, instrument, expiry_str)

    return r


def get_option_chain_table(symbol, instrument=None, expiry=None):
    optchainscrape = get_option_chain(symbol, instrument, expiry)
    html_soup = BeautifulSoup(optchainscrape.text, 'html.parser')
    sptable = html_soup.find("table", {"id": "octable"})
    tp = ParseTables(soup=sptable,
                     schema=OPTIONS_CHAIN_SCHEMA,
                     headers=OPTIONS_CHAIN_HEADERS, index=OPTIONS_CHAIN_INDEX)
    return tp.get_df()


def get_futures_chain(symbol):
    r = futures_chain_url(symbol)
    return r


def get_futures_chain_table(symbol):
    futuresscrape = get_futures_chain(symbol)
    html_soup = BeautifulSoup(futuresscrape.text, 'html.parser')
    spdiv = html_soup.find("div", {"id": "tab26Content"})
    sptable = spdiv.find("table")
    tp = ParseTables(soup=sptable, schema=FUTURES_SCHEMA,
                     headers=FUTURES_HEADERS, index=FUTURES_INDEX)
    return tp.get_df()


def get_holidays_list(fromDate,
                      toDate):
    """This is the function to get exchange holiday list between 2 dates.
        Args:
            fromDate (datetime.date): start date
            toDate (datetime.date): end date
        Returns:
            pandas.DataFrame : A pandas dataframe object
        Raises:
            ValueError:
                        1. From Date param is greater than To Date param
    """
    if fromDate > toDate:
        raise ValueError('Please check start and end dates')

    holidayscrape = holiday_list_url(fromDate.strftime(
        "%d-%m-%Y"), toDate.strftime("%d-%m-%Y"))
    html_soup = BeautifulSoup(holidayscrape.text, 'lxml')
    sptable = html_soup.find("table")
    tp = ParseTables(soup=sptable,
                     schema=[str, StrDate.default_format(
                         format="%d-%b-%Y"), str, str],
                     headers=["Market Segment", "Date", "Day", "Description"], index="Date")
    dfret = tp.get_df()
    dfret = dfret.drop(["Market Segment"], axis=1)
    return dfret


def isworkingday(dt):
    """This is the function to check if a given date is a working day
        Args:
            dt (datetime.date): Date to Check
        Returns:
            bool 
    """
    weekday = dt.isoweekday()
    if weekday in (6, 7):
        return False
    else:
        lsholiday = get_holidays_list(dt, dt)
        # pdb.set_trace()
        if dt in lsholiday.index:
            return False

    return True


def nextworkingday(dt):
    """This is the function to get the next working day after the given date
        Args:
            dt (datetime.date): Date to Check
        Returns:
            dt (datetime.date): Nearest working day after the given date
    """
    dttmp = dt
    while True:
        dttmp = dttmp + dateutil.relativedelta.relativedelta(days=1)
        if isworkingday(dttmp):
            return dttmp


def previousworkingday(dt):
    """This is the function to get the last working day before the given date
        Args:
            dt (datetime.date): Date to Check
        Returns:
            dt (datetime.date): Nearest working day before the given date
    """

    dttmp = dt
    while True:
        dttmp = dttmp - dateutil.relativedelta.relativedelta(days=1)
        if isworkingday(dttmp):
            return dttmp


def getworkingdays(dtfrom, dtto):
    # pdb.set_trace()
    dfholiday = get_holidays_list(dtfrom, dtto)
    stalldays = set()
    stweekends = set()

    for i in range((dtto - dtfrom).days + 1):
        dt = dtfrom + datetime.timedelta(days=i)
        stalldays.add(dt)

        if dt.isoweekday() in (6, 7):
            stweekends.add(dt)

    # pdb.set_trace()
    stspecial  = set(
      [datetime.date(2020,2,1) # Budget day
      ]
    )

    #Remove special weekend working days from weekends set
    stweekends -= stspecial
    stworking = (stalldays - stweekends) - set(dfholiday.index.values)
    # stworking = (stalldays - stweekends) - set(dfholiday.index.values)

    # #Special cases where market was open on weekends
    # stspecial  = set(
      # [datetime.date(2020,2,1) # Budget day
      # ]
    # )
    # for dtspecial in stspecial:
      # if (dtspecial >= dtfrom and dtspecial <= dtto):
        # stworking.add(dtspecial)

    return sorted(stworking)