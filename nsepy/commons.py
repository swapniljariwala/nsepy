# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 23:12:26 2015

@author: jerry
"""
import requests
from nsepy.constants import NSE_INDICES, INDEX_DERIVATIVE, DERIVATIVE_TO_INDEX
import datetime
from functools import partial
import pandas as pd
import StringIO
import zipfile
import threading
import six
import sys
def is_index(index):
    return index in NSE_INDICES


def is_index_derivative(index):
    return index in INDEX_DERIVATIVES



class StrDate(datetime.date):
    """
    for pattern-
        https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
        
    """
    def __new__(cls, string, format):
        dt = datetime.datetime.strptime(string, format)        
        return datetime.date.__new__(datetime.date, dt.year, dt.month, dt.day)
    
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
        
        
        

class URLFetch(requests.Session):
    def __init__(self):
        super.__init__(self)


class ParseTables:
    def __init__(self, *args, **kwargs):
        self.schema = kwargs.get('schema')
        self.bs = kwargs.get('soup')
        self.headers = kwargs.get('headers')
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
                    val = schema[i](txt)
                    lst.append(val)
                lists.append(lst)
        self.lists = lists
    
    def get_tables(self):
        return self.lists
    
    def get_df(self):
        return pd.DataFrame(self.lists)

def unzip_str(zipped_str, file_name = None):
    fp = StringIO.StringIO(zipped_str)
    zf = zipfile.ZipFile(file = fp)
    if not file_name:
        file_name = zf.namelist()[0]
    return zf.read(file_name)

class ThreadReturns(threading.Thread):
    def run(self):
        if sys.version_info[0] == 2:
            self.result = self._Thread__target(*self._Thread__args, **self._Thread__kwargs)
        else: # assuming v3
            self.result = self._target(*self._args, **self._kwargs)
            
        