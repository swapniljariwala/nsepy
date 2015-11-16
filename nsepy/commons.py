# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 23:12:26 2015

@author: jerry
"""
import requests
from nsepy.constants import NSE_INDICES, INDEX_DERIVATIVE

def is_index(index):
    return index in NSE_INDICES

def is_index_derivative(index):
    return index in INDEX_DERIVATIVE.keys()


class StrDate(datetime.date):
    """
    for pattern-
        https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
        
    """
    def __init__(self, string, format):
        pass
        
        
        

class URLFetch(requests.Session):
    def __init__(self):
        super.__init__(self)


class ParseTables:
    def __init__(self, *args, **kwargs):
        pass