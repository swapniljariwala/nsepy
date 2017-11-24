# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:57:53 2015

@author: Swapnil Jariwala
"""
from nsepy.history import validate_params
from nsepy.urls import get_symbol_count
from nsepy import urls
from nsepy import history
from nsepy.nselist import nse_to_icici
import unittest
from datetime import date
import six
class TestHistory(unittest.TestCase):
    def setUp(self):
        self.start = date(2015,1,1)
        self.end = date(2015,1,10)

    def test_validate_params(self):
        #test stock history param validation
        (url, params, schema,
         headers, scaling) = validate_params(symbol='SBIN',
                                             start=date(2014,1,1),
                                             end=date(2014,1,10))
                                                    
        params_ref = {"symbol":"SBIN", "symbolCount":'1',
                  "series":"EQ", "fromDate":"01-01-2014",
                  "toDate":"10-01-2014"}
        self.assertEqual(params, params_ref)
        self.assertEqual(url, urls.equity_history_url)
        self.assertEqual(schema, history.EQUITY_SCHEMA)
        
        #test index history params
        """
        1. indexType=index name
        2. fromDate string dd-mm-yyyy
        3. toDate string dd-mm-yyyy
        """
        params = {"indexType":"NIFTY 50", 
                  "fromDate":"01-01-2014",
                  "toDate":"10-01-2014"}
        self.assertEqual(params, validate_params(symbol='NIFTY 50',
                                index=True,
                                start=date(2014,1,1),
                                end=date(2014,1,10))[1])
        
        #test index options params
        """
        instrumentType=OPTIDX
        symbol=NIFTY
        expiryDate=26-11-2015
        optionType=select
        strikePrice=
        dateRange=15days
        fromDate= 01-Nov-2015
        toDate=19-Nov-2015
        segmentLink=9&
        symbolCount=
        """
        params = {"instrumentType":"OPTIDX",
                  "symbol":"NIFTY",
                  "expiryDate":"26-11-2015",
                  "optionType":"CE",
                  "strikePrice":7800,
                  "dateRange":"",
                  "fromDate":"01-Nov-2015",
                  "toDate":"19-Nov-2015"}
        self.assertEqual(params, validate_params(symbol="NIFTY",
                                                index=True,
                                                option_type = "CE",
                                                expiry_date=date(2015,11,26),
                                                start=date(2015,11,1),
                                                end=date(2015,11,19),
                                                strike_price=7800)[1])
        
        negative_args = []
        #start>end
        negative_args.append({'symbol':'SBIN', 'start': date(2014,1,10),
                              'end':date(2014,1,1)})
        #expiry date missing for future contract
        negative_args.append({'symbol':'SBIN', 'start': date(2014,1,1),
                              'end':date(2014,1,11), 'futures':True})
        #Strike price missing for options
        negative_args.append({'symbol':'SBIN', 'start': date(2014,1,1),
                              'end':date(2014,1,11), 'option_type':'CE'})
        #option_type!=None and futures=True
        negative_args.append({'symbol':'SBIN', 'start': date(2014,1,1),
                              'end':date(2014,1,11), 
                              'option_type':'CE', 'futures':True})
        #test for exceptions
        for n_arg in negative_args:
            with self.assertRaises(ValueError):
                validate_params(**n_arg)
        

        
            

if __name__ == '__main__':
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHistory)
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
        
        
