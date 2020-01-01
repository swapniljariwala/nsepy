import datetime
import unittest
import json
import requests
import six

from bs4 import BeautifulSoup

from tests import htmls
from nsepy.liveurls import quote_eq_url, quote_derivative_url, option_chain_url, futures_chain_url, holiday_list_url
import nsepy.urls as urls
from nsepy.commons import (is_index, is_index_derivative,
                           NSE_INDICES, INDEX_DERIVATIVES,
                           ParseTables, StrDate, unzip_str,
                           ThreadReturns, URLFetch)


class TestLiveUrls(unittest.TestCase):
    def setUp(self):
        proxy_on = False
        if proxy_on:
            urls.session.proxies.update({'http': 'proxy1.wipro.com:8080'})

    def runTest(self):
        for key in TestUrls.__dict__.keys():
            if key.find('test') == 0:
                TestUrls.__dict__[key](self)

    def test_quote_eq_url(self):
        resp = quote_eq_url('SBIN', 'EQ')
        html_soup = BeautifulSoup(resp.text, 'lxml')
        hresponseDiv = html_soup.find("div", {"id": "responseDiv"})
        d = json.loads(hresponseDiv.get_text())
        self.assertEqual(d['data'][0]['symbol'], 'SBIN')

    def test_quote_derivative_url(self):
        resp = quote_derivative_url("NIFTY", "FUTIDX", "30JAN2020", '-', '-')
        html_soup = BeautifulSoup(resp.text, 'lxml')
        hresponseDiv = html_soup.find("div", {"id": "responseDiv"})
        d = json.loads(hresponseDiv.get_text().strip())
        self.assertEqual(d['data'][0]['underlying'], 'NIFTY')

    def test_option_chain_url(self):
        """
            1. Underlying symbol
            2. instrument (FUTSTK, OPTSTK, FUTIDX, OPTIDX)
            3. expiry date (ddMMMyyyy) where dd is not padded with zero when date is single digit
        """

        resp = option_chain_url('SBIN', 'OPTSTK', '30JAN2020')
        self.assertGreaterEqual(resp.text.find('Open Interest'), 0)

    def test_futures_chain_url(self):
        """
            1. Underlying symbol
        """

        resp = futures_chain_url('NIFTY')
        self.assertGreaterEqual(resp.text.find('Expiry Date'), 0)

    def test_holiday_list_url(self):
        resp = holiday_list_url("01Jan2019", "31Mar2019")
        self.assertGreaterEqual(resp.text.find('Holi'), 0)
