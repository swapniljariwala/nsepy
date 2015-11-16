# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 23:12:26 2015

@author: jerry
"""
import requests
from nsepy.constants import NSE_INDICES, INDEX_DERIVATIVE
import datetime
from functools import partial
def is_index(index):
    return index in NSE_INDICES

def is_index_derivative(index):
    return index in INDEX_DERIVATIVE.keys()


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
    
    def get_tables(self):
        trs = self.bs.find_all('tr')
        lists = []
        schema = self.schema
        #r_cnt = 0
        for tr in trs:
            tds = tr.find_all('td')
            if len(tds) == len(schema):
                for i in range(0, len(tds)):
                    txt = tds[i].text.replace('\n','').replace(' ','').replace(',','')
                    try:
                        lists[i].append(schema[i](txt))
                    except:
                        lists.append([])
                        lists[i].append(schema[i](txt))
        
        return lists
                    
            
        