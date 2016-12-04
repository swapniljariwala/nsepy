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
import six
from nsepy.urls import *
import nsepy.urls as urls
import urlparse

class TestUrls(unittest.TestCase):
    def setUp(self):
        proxy_on = False
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

    def test_price_list_url(self):
        date_str = "11-19-2015"
        resp = price_list_url('2015', 'NOV', '19NOV2015')
        csv = unzip_str(resp.content)
        self.assertGreaterEqual(csv.find('SBIN'),0)

    def tests_daily_volatility_url(self):
        resp = daily_volatility_url("19112015")
        self.assertGreaterEqual(resp.text.find('SBIN'),0)

    def test_pr_price_list_zipped_url(self):
        resp = pr_price_list_zipped_url('191115')
        csv = unzip_str(resp.content)

    def test_index_history_url(self):
        resp = index_history_url(indexType="NIFTY 50",
                                 fromDate="01-01-2015",
                                 toDate="10-01-2015")
        self.assertGreaterEqual(resp.text.find('High'),0)
        self.assertGreaterEqual(resp.text.find('Low'),0)

    def test_index_pe_history_url(self):
        resp = index_pe_history_url(fromDate="01-01-2015",
                                    toDate="10-01-2015",
                                    indexName="NIFTY 50")
        self.assertGreaterEqual(resp.text.find('<th>P/E'),0)
        self.assertGreaterEqual(resp.text.find('<th>P/B'),0)

    def test_index_vix_history_url(self):
        resp = index_vix_history_url(fromDate="01-Jan-2015",
                                    toDate="10-Jan-2015",
                                    )
        self.assertGreaterEqual(resp.text.find('VIX'),0)
        self.assertGreaterEqual(resp.text.find('Change'),0)

    def test_derivative_derivative_expiry_dates_url(self):
        resp = derivative_expiry_dates_url()
        self.assertGreaterEqual(resp.text.find('vixExpryDt'),0)

    def test_derivative_history_url(self):
        resp = derivative_history_url(instrumentType="FUTIDX",
                                      symbol="NIFTY",
                                      expiryDate="26-11-2015",
                                      optionType="select",
                                      strikePrice='',
                                      dateRange='',
                                      fromDate='01-Nov-2015',
                                      toDate="19-Nov-2015")
        self.assertGreaterEqual(resp.text.find('NIFTY'),0)
        self.assertGreaterEqual(resp.text.find('Expiry'),0)

    def test_derivative_price_list_url(self):
        resp = derivative_price_list_url('2015','NOV','19NOV2015')
        csv = unzip_str(resp.content)


if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(TestUrls)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if six.PY2:
        if result.wasSuccessful():
            print("tests OK")
        for (test, error) in result.errors:
            print("=========Error in: %s==========="%test)
            print(error)
            print("======================================")

        for (test, failures) in result.failures:
            print("=========Error in: %s==========="%test)
            print(failures)
            print("======================================")
