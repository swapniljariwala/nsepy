# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 23:12:26 2015

@author: jerry
"""
import requests
import csv
from nsepy.constants import NSE_INDICES, INDEX_DERIVATIVES, DERIVATIVE_TO_INDEX
import datetime
from dateutil.parser import parse
from functools import partial
try:
    import pandas as pd
except ImportError:
    pass

import zipfile
import threading
import six
import sys
import numpy as np
import six
from bs4 import BeautifulSoup
if six.PY3:
    from urllib.request import build_opener, HTTPCookieProcessor, Request
    from http.cookiejar import CookieJar
    from functools import lru_cache
else:
    from urllib2 import HTTPCookieProcessor, Request, build_opener
    from cookielib import CookieJar
    from backports.functools_lru_cache import lru_cache
import re
import sys

from six.moves.urllib.parse import urlparse


def is_index(index):
    return index in NSE_INDICES

def is_index_derivative(index):
    return index in INDEX_DERIVATIVES

months = ["Unknown",
    "January",
    "Febuary",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]


class StrDate(datetime.date):
    """
    for pattern-
        https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior

    """
    def __new__(cls, date, format):

        if(isinstance(date,datetime.date)):
            return datetime.date.__new__(datetime.date, date.year,
                                         date.month, date.day)
        dt = datetime.datetime.strptime(date, format)
        return datetime.date.__new__(datetime.date, dt.year,
                                     dt.month, dt.day)

    @classmethod
    def default_format(cls, format):
        """
        returns a new class with a default parameter format in the __new__
        method. so that string conversions would be simple in TableParsing with
        single parameter
        """
        class Date_Formatted(cls):
            pass
        Date_Formatted.__new__ = partial(cls.__new__, format = format)
        return Date_Formatted


class ParseTables:
    def __init__(self, *args, **kwargs):
        self.schema = kwargs.get('schema')
        self.bs = kwargs.get('soup')
        self.headers = kwargs.get('headers')
        self.index = kwargs.get('index')
        self._parse()

    def _parse(self):
        trs = self.bs.find_all('tr')
        lists = []
        schema = self.schema
        for tr in trs:
            tds = tr.find_all('td')
            if len(tds) == len(schema):
                lst = []
                for i in range(0, len(tds)):
                    txt = tds[i].text.replace('\n','').replace(' ','').replace(',','')
                    try:
                        val = schema[i](txt)
                    except:
                        if schema[i]==float or schema[i]==int:
                            val = np.nan
                        else:
                            val = ''
                            #raise ValueError("Error in %d. %s(%s)"%(i, str(schema[i]), txt))
                    lst.append(val)
                lists.append(lst)
        self.lists = lists

    def get_tables(self):
        return self.lists

    def get_df(self):
        if self.index:
            return pd.DataFrame(self.lists, columns=self.headers).set_index(self.index)
        else:
            return pd.DataFrame(self.lists, columns=self.headers)

def unzip_str(zipped_str, file_name = None):
    if isinstance(zipped_str, six.binary_type):
        fp = six.BytesIO(zipped_str)
    else:
        fp = six.BytesIO(six.b(zipped_str))

    zf = zipfile.ZipFile(file=fp)
    if not file_name:
        file_name = zf.namelist()[0]
    return zf.read(file_name).decode('utf-8')

class ThreadReturns(threading.Thread):
    def run(self):
        if sys.version_info[0] == 2:
            self.result = self._Thread__target(*self._Thread__args, **self._Thread__kwargs)
        else: # assuming v3
            self.result = self._target(*self._args, **self._kwargs)

class URLFetch:

    def __init__(self, url, method='get', json=False, session=None,
                 headers = None, proxy = None):
        self.url = url
        self.method = method
        self.json = json

        if not session:
            self.session = requests.Session()
        else:
            self.session = session

        if headers:
            self.session.headers.update(headers)
        if proxy:
            self.update_proxy(proxy)
        else:
            self.update_proxy('')

    def set_session(self, session):
        self.session = session
        return self

    def get_session(self, session):
        self.session = session
        return self

    def __call__(self, *args, **kwargs):
        u = urlparse(self.url)
        self.session.headers.update({'Host': u.hostname})
        url = self.url%(args)
        if self.method == 'get':
            return self.session.get(url, params=kwargs, proxies = self.proxy )
        elif self.method == 'post':
            if self.json:
                return self.session.post(url, json=kwargs, proxies = self.proxy )
            else:
                return self.session.post(url, data=kwargs, proxies = self.proxy )

    def update_proxy(self, proxy):
        self.proxy = proxy
        self.session.proxies.update(self.proxy)

    def update_headers(self, headers):
        self.session.headers.update(headers)



def byte_adaptor(fbuffer):
    """ provides py3 compatibility by converting byte based
    file stream to string based file stream
    Arguments:
        fbuffer: file like objects containing bytes
    Returns:
        string buffer
    """
    if six.PY3:
        strings = fbuffer.read().decode('utf-8')
        fbuffer = six.StringIO(strings)
        return fbuffer
    else:
        return fbuffer


def js_adaptor(buffer):
    """ convert javascript objects like true, none, NaN etc. to
    quoted word.
    Arguments:
        buffer: string to be converted
    Returns:
        string after conversion
    """
    buffer = re.sub('true', 'True', buffer)
    buffer = re.sub('false', 'False', buffer)
    buffer = re.sub('none', 'None', buffer)
    buffer = re.sub('NaN', '"NaN"', buffer)
    return buffer



class NseHolidays():
    """
    Contains methods to parse and extract data about the holidays of NSE
    """

    def get_holiday_list(self):
        """
        Cleans the holiday list
        """
        holiday_list = self.__parse_holiday_list__()
        clean_holiday_list = []
        for item in holiday_list:
            individual_data = []
            # Each row is separated by commas.
            reader = csv.reader(item, delimiter=',')
            for row in reader:
                individual_data.append(row)
            clean_holiday_list.append(individual_data[:2])
        previous = 0
        holiday_list = []
        # These are all the holidays excluding saturdays and sundays
        todays_date = datetime.datetime.now().date()
        for  series in clean_holiday_list:
            # We wish to extract only the trading holidays.
            # The serial number resets after trading holidays i.e when it moves to clearing holidays
            if previous < int(series[0][0]):
                # Convert to datetime format
                parsed_date = parse(series[1][0])
                if todays_date <= parsed_date.date():
                    holiday_list.append(parsed_date.date())
                previous += 1

        # We will now extract the saturdays and sundays
        date = todays_date
        date += datetime.timedelta(days=6-date.weekday())
        diff = date - datetime.timedelta(days=1)
        while date.year == todays_date.year:
            holiday_list.append(diff)
            holiday_list.append(date)
            date += datetime.timedelta(days=7)
            diff += datetime.timedelta(days=7)

        # This is the final holiday list from the current time.
        return holiday_list

    @lru_cache(maxsize=2)
    def __parse_holiday_list__(self):
        """
        :Returns: a list of all the holidays with the serial number, date and holiday name
        """

        # TODO: clean this. There has to be a reusable way to read urls and retreive reponses from
        # them
        def __read_url__(url, headers):
            """
            Reads the url, processes it and returns a StringIO object to aid reading
            :Parameters:
            url: str
                the url to request and read from
            headers: dict
                The right set of headers for requesting from http://nseindia.com
            :returns: _io.StringIO object of the response
            """
            cookie_jar = CookieJar()
            opener =  build_opener(HTTPCookieProcessor(cookie_jar))
            request = Request(url, None, headers)
            response = opener.open(request)

            if response is not None:
                return byte_adaptor(response)
            else:
                raise Exception('No response received')
        # Parse the holiday url and extract useful details
        headers = {'Accept': '*/*',
                   'Accept-Language': 'en-US,en;q=0.5',
                   'Host': 'nseindia.com',
                   'Referer': "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=INFY&illiquid=0&smeFlag=0&itpFlag=0",
                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
                   'X-Requested-With': 'XMLHttpRequest'
                   }
        holiday_url = 'https://www.nseindia.com/products/content/equities/equities/mrkt_timing_holidays.htm'
        res = __read_url__(holiday_url, headers)
        res = res.read()

        soup = BeautifulSoup(res, 'html.parser')
        holiday_list = []
        # The data is stored in tables. Extract only the tabular data
        for row in soup.find_all('tr', recursive=False):
            record = [td.text.replace(',', '') for td in row.find_all('td')]
            holiday_list.append(record)

        return holiday_list

def conditional_decorator(decorator, condition):
    def res_decorator(f):
        if not condition:
            return f
        return decorator(f)
    return res_decorator

def market_status():
    """
    Checks whether the market is open or not
    :returns: bool variable indicating status of market. True -> Open, False -> Closed
    """
    nse_holidays = NseHolidays()
    holiday_list = nse_holidays.get_holiday_list()

    # Check if today is a holiday according to the holiday list.
    if datetime.datetime.now().date() in holiday_list:
        return False

    current_time = datetime.datetime.now().time()
    # Check if the current time is in the time bracket in which NSE operates.
    # The market opens at 9:15 am
    start_time = datetime.datetime.now().time().replace(hour=9, minute=15, second=0, microsecond=0)
    # And ends at 3:30 = 15:30
    end_time = datetime.datetime.now().time().replace(hour=15, minute=30, second=0, microsecond=0)

    if current_time > start_time and current_time < end_time:
        return True

    # In case the above condition does not satisfy, the default value (False) is returned
    return False