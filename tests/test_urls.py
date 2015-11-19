# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:52:33 2015

@author: SW274998
"""

from nsepy.commons import (is_index, is_index_derivative,
                           NSE_INDICES, INDEX_DERIVATIVES,
                           ParseTables, StrDate, unzip_str,
                           ThreadReturns, URLFetch)
import datetime
import unittest
from bs4 import BeautifulSoup
from tests import htmls
import json
import requests

from nsepy.urls import *
import nsepy.urls as urls


class TestUrls(unittest.TestCase):
    def setUp(self):
        proxy_on = True
        if proxy_on:
            urls.session.proxies.update({'http':'proxy1.wipro.com:8080'})
    
    def runTest(self):
        for key in TestUrls.__dict__.keys():
            if key.find('test') == 0:
                TestUrls.__dict__[key](self)

    def test_get_symbol_count(self):
        count = get_symbol_count(symbol='SBIN')
        self.assertEqual(count,'1')

    def test_equity_history_url(self):
        sym_count = get_symbol_count(symbol='SBIN')
        txt = 'Data for SBIN - EQ'
        resp = equity_history_url(symbol='SBIN',
                                  symbolCount=sym_count,
                                  series='EQ',
                                  fromDate='01-01-2000',
                                  toDate='10-01-2000',
                                  dateRange='')
        self.assertGreaterEqual(resp.text.find(txt),0, resp.text)

if __name__ == '__main__':
    
    unittest.main()
        