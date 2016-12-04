# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 23:12:26 2015

@author: jerry
"""
import requests
from nsepy.constants import NSE_INDICES, INDEX_DERIVATIVES, DERIVATIVE_TO_INDEX
import datetime
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
