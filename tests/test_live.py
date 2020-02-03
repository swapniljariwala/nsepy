import datetime
import unittest
import json
import pdb
import requests
import six

from bs4 import BeautifulSoup

from tests import htmls
from nsepy.liveurls import quote_eq_url, quote_derivative_url, option_chain_url, futures_chain_url
from nsepy.live import get_quote, get_futures_chain_table, get_holidays_list, isworkingday, nextworkingday, previousworkingday, getworkingdays
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
        comp_name = q['data'][0]['companyName']
        self.assertEqual(comp_name, "State Bank of India")

    def test_get_quote_stock_der(self):
        """
        1. Underlying security (stock symbol or index name)
        2. instrument (FUTSTK, OPTSTK, FUTIDX, OPTIDX)
        3. expiry (ddMMMyyyy)
        4. type (CE/PE for options, - for futures
        5. strike (strike price upto two decimal places
        """
        n = datetime.datetime.now()
        stexp = get_expiry_date(n.year, n.month, index=False, stock=True)
        self.assertEqual(len(stexp), 1)

        if n.date() > list(stexp)[0]:
            try:
                stexp = get_expiry_date(
                    n.year, n.month + 1, index=False, stock=True)
            except:
                stexp = get_expiry_date(n.year + 1, 1, index=False, stock=True)

        self.assertEqual(len(stexp), 1)
        exp = min([x for x in stexp if x > n.date()])
        q = get_quote(symbol='SBIN', instrument='FUTSTK', expiry=exp)
        comp_name = q['data'][0]['instrumentType']
        self.assertEqual(comp_name, "FUTSTK")

        exp = min([x for x in stexp if x > n.date()])
        q = get_quote(symbol='SBIN', instrument='OPTSTK',
                      expiry=exp, option_type="CE", strike=300)
        comp_name = q['data'][0]['instrumentType']
        self.assertEqual(comp_name, "OPTSTK")

    def test_get_quote_index_der(self):
        """
        1. Underlying security (stock symbol or index name)
        2. instrument (FUTSTK, OPTSTK, FUTIDX, OPTIDX)
        3. expiry (ddMMMyyyy)
        4. type (CE/PE for options, - for futures
        5. strike (strike price upto two decimal places
        """
        n = datetime.datetime.now()
        stexp = get_expiry_date(n.year, n.month)
        # 4 weekly expiry per month
        # Corner case where 1 Feb is a holiday and its non-leap year Feb will only get 3 expiries in the month
        # So test for only >=3
        self.assertGreaterEqual(len(stexp), 3)

        if n.date() > max(stexp):
            try:
                stexp = get_expiry_date(n.year, n.month + 1)
            except:
                stexp = get_expiry_date(n.year + 1, 1)

        self.assertGreaterEqual(len(stexp), 3)

        exp = max([x for x in stexp if x > n.date()])
        q = get_quote(symbol='NIFTY', instrument='FUTIDX', expiry=exp)
        comp_name = q['data'][0]['instrumentType']
        self.assertEqual(comp_name, "FUTIDX")

        exp = min([x for x in stexp if x > n.date()])
        q = get_quote(symbol='NIFTY', instrument='OPTIDX',
                      expiry=exp, option_type="CE", strike=11000)
        comp_name = q['data'][0]['instrumentType']
        self.assertEqual(comp_name, "OPTIDX")

    def test_get_futures_chain(self):
        """
        1. Underlying security (stock symbol or index name)
        """
        n = datetime.datetime.now()
        dftable = get_futures_chain_table('NIFTY')

        # Atleast 3 expiry sets should be open
        self.assertGreaterEqual(len(dftable), 3)

        (dtnear, dtnext, dtfar) = dftable.index.tolist()
        self.assertLess(dtnear, dtnext)
        self.assertLess(dtnext, dtfar)

    def test_get_holiday_list(self):
        """
        Check holiday list for first quarter for 2019 against the expected data
        -----------------------------------------------------------
        Date               Day Of the Week             Description
        ------------------------------------------------------------
        2019-03-04          Monday           Mahashivratri
        2019-03-21        Thursday                    Holi
        """
        fromdate = datetime.date(2019, 1, 1)
        todate = datetime.date(2019, 3, 31)
        lstholiday = get_holidays_list(fromdate, todate)
        self.assertEqual(len(lstholiday), 2)
        self.assertFalse(
            lstholiday[lstholiday['Description'] == "Mahashivratri"].empty)
        self.assertFalse(
            lstholiday[lstholiday['Day'] == "Thursday"].empty)

    def test_working_day(self):
        # shivratri
        shivratri = datetime.date(2019, 3, 4)
        self.assertFalse(isworkingday(shivratri))
        self.assertTrue(nextworkingday(shivratri), datetime.date(2019, 3, 5))
        self.assertTrue(previousworkingday(shivratri),
                        datetime.date(2019, 3, 1))

    def test_working_day(self):
        # 20 to 28th aug
        independenceday = datetime.date(2019, 8, 15)
        workingdays = getworkingdays(datetime.date(
            2019, 8, 13), datetime.date(2019, 8, 17))
        self.assertFalse(independenceday in workingdays)
        self.assertEqual(len(workingdays), 3)

        # working days in March 2019
        # 31 day month with 2 holidays
        workingdays = getworkingdays(datetime.date(
            2019, 3, 1), datetime.date(2019, 3, 31))
        self.assertEqual(len(workingdays), 19)

        # working day for special dates on weekend
        workingdays = getworkingdays(datetime.date(
            2020, 1, 31), datetime.date(2020, 2, 3))
        self.assertEqual(len(workingdays), 3)
        