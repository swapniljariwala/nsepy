import datetime
import unittest
#import urlparse
import json
import requests
import six

from bs4 import BeautifulSoup

from tests import htmls
from nsepy.liveurls import quote_eq_url, quote_derivative_url, option_chain_url
from nsepy.live import get_quote
import nsepy.urls as urls
from nsepy.commons import (is_index, is_index_derivative,
                           NSE_INDICES, INDEX_DERIVATIVES,
                           ParseTables, StrDate, unzip_str,
                           ThreadReturns, URLFetch)
from nsepy import get_expiry_date

class TestLiveUrls(unittest.TestCase):
    def setUp(self):
        pass

    def runTest(self):
        for key in TestUrls.__dict__.keys():
            if key.find('test') == 0:
                TestUrls.__dict__[key](self)

    def test_get_quote_eq(self):
        q = get_quote(symbol='SBIN')
        comp_name = q['companyName']
        self.assertEqual(comp_name, "State Bank of India")

    def test_get_quote_der(self):

        """
        1. Underlying security (stock symbol or index name)
        2. instrument (FUTSTK, OPTSTK, FUTIDX, OPTIDX)
        3. expiry (ddMMMyyyy)
        4. type (CE/PE for options, - for futures
        5. strike (strike price upto two decimal places
        """
        n = datetime.datetime.now()
        exp = get_expiry_date(n.year, n.month)
        
        if n.date() > exp:
            try:
                exp = get_expiry_date(n.year, n.month + 1)
            except:
                exp = get_expiry_date(n.year + 1, 1)
        
        
        q = get_quote(symbol='SBIN', instrument='FUTSTK', expiry=exp)
        comp_name = q['instrumentType']
        self.assertEqual(comp_name, "FUTSTK")




