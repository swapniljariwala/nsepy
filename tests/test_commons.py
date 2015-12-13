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
import urlparse
import nsepy.urls
import six
def text_to_list(text, schema):
    rows = text.split('\n')
    lists = []
    for row in rows:
        if not row:
            continue
        cols = row.split(',')
        i = 0
        lst = []
        for cell in cols:
            lst.append(schema[i](cell))
            i += 1
        lists.append(lst)
    """
    for i in range(0, len(lists)):
        for j in range(0, len(lists[i])):
            lists[i][j] = schema[i](lists[i][j])
    """
    return lists


class TestCommons(unittest.TestCase):
    def setUp(self):
        pass

    def test_is_index(self):
        for i in NSE_INDICES:
            self.assertTrue(is_index(i))

    def test_is_index_derivative(self):
        for i in INDEX_DERIVATIVES:
            self.assertTrue(is_index_derivative(i))

    def test_ParseTables(self):
        # test equity tables
        
        dd_mmm_yyyy = StrDate.default_format(format="%d-%b-%Y")
        schema = [str, str,
                  dd_mmm_yyyy,
                  float, float, float, float,
                  float, float, float, int, float,
                  int, int, float]
        bs = BeautifulSoup(htmls.html_equity)
        t = ParseTables(soup=bs,
                        schema=schema)
        lst = text_to_list(htmls.csv_equity, schema=schema)
        self.assertEqual(lst, t.get_tables())
        
        #test derivative tables
        schema = [str, dd_mmm_yyyy, dd_mmm_yyyy,
                  float, float, float, float,
                  float, float, int, float,
                  int, int, float]
        bs = BeautifulSoup(htmls.html_derivative)
        t = ParseTables(soup=bs,
                        schema=schema)
        lst = text_to_list(htmls.csv_derivative, schema)
        self.assertEqual(lst, t.get_tables())
        
        #test index tables
        schema = [dd_mmm_yyyy,
                  float, float, float, float,
                  int, float]
        bs = BeautifulSoup(htmls.html_index)
        t = ParseTables(soup=bs,
                        schema=schema)
        lst = text_to_list(htmls.csv_index, schema)
        self.assertEqual(lst, t.get_tables())
    
    def test_ParseTables_headers(self):
        # test equity tables
        dd_mmm_yyyy = StrDate.default_format(format="%d-%b-%Y")
        # schema for equity history values
        schema = [str, str,
                  dd_mmm_yyyy,
                  float, float, float, float,
                  float, float, float, int, float,
                  int, int, float]
        headers = ["Symbol", "Series", "Date", "Prev Close", 
                  "Open", "High", "Low","Last", "Close", "VWAP",
                  "Volume", "Turnover", "Trades", "Deliverable Volume",
                  "%Deliverble"]
        bs = BeautifulSoup(htmls.html_equity)
        t = ParseTables(soup=bs,
                        schema=schema, headers=headers,index='Date')
        lst = text_to_list(htmls.csv_equity, schema)
        df = t.get_df()
        self.assertIn("Symbol",df.columns, str(df.columns))
        
    def test_StrDate(self):
        dd_mmm_yyyy = StrDate.default_format(format="%d-%b-%Y")
        dt1 = dd_mmm_yyyy(date= "12-Nov-2012")
        dt2 = datetime.date(2012, 11, 12)
        self.assertEqual(dt1, dt2)
    
    def test_unzip_str(self):
        self.assertEqual(htmls.unzipped, unzip_str(htmls.zipped))
    
    def test_ThreadReturns(self):
        def square(ip):
            return ip**2
        t1 = ThreadReturns(target = square, kwargs = {'ip':2})
        t1.start()
        t1.join()
        self.assertEquals(t1.result, 4)
    
   
class TestURLFetch(unittest.TestCase):
    def setUp(self):
        self.proxy_on = False
        self.session = requests.Session()
        if self.proxy_on:
            self.session.proxies.update({'http':'proxy1.wipro.com:8080', 'https':'proxy.wipro.com:8080'})        
        self.session.headers.update({'User-Agent' : 'Testing'})
    
    def test_get(self):
        url = 'http://httpbin.org/get'
        http_get = URLFetch(url=url, session=self.session)
        try:
            resp = http_get(key1='val1', key2='val2')
        except requests.exceptions.ConnectionError as e:
            raise requests.exceptions.ConnectionError('Error fetching (check proxy settings):',url)
        json = resp.json()
        self.assertEqual(json['args']['key1'], 'val1')
        self.assertEqual(json['args']['key2'], 'val2')
    
    def test_urls_with_args_and_data(self):
        url = 'http://httpbin.org/%s'
        http_post = URLFetch(url=url, method='post', session=self.session)
        try:
            resp = http_post('post', key1='val1', key2='val2')
        except requests.exceptions.ConnectionError as e:
            raise requests.exceptions.ConnectionError('Error fetching (check proxy settings):',url)
        rjson = resp.json()
        self.assertEqual(rjson['form']['key1'], 'val1')
        self.assertEqual(rjson['form']['key2'], 'val2')

    def test_post(self):
        url = 'http://httpbin.org/post'
        http_post = URLFetch(url=url, method='post', session=self.session)
        try:
            resp = http_post(key1='val1', key2='val2')
        except requests.exceptions.ConnectionError as e:
            raise requests.exceptions.ConnectionError('Error fetching (check proxy settings):',url)
        rjson = resp.json()
        self.assertEqual(rjson['form']['key1'], 'val1')
        self.assertEqual(rjson['form']['key2'], 'val2')

    def test_json(self):
        url = 'http://httpbin.org/post'
        http_get = URLFetch(url=url, method='post', json=True, session=self.session)
        try:
            resp = http_get(key1='val1', key2='val2')
        except requests.exceptions.ConnectionError as e:
            raise requests.exceptions.ConnectionError('Error fetching (check proxy settings):',url)
        rjson = resp.json()
        
        self.assertEqual(json.loads(rjson['data']), {u'key1':u'val1',
                                                             u'key2':u'val2'} )
        
    def test_cookies(self):
        url = 'http://httpbin.org/cookies/set'
        http_cookie = URLFetch(url=url, session=self.session)
        try:
            resp = http_cookie(var1=1,var2='a')
        except requests.exceptions.ConnectionError as e:
            raise requests.exceptions.ConnectionError('Error fetching (check proxy settings):',url)
        rjson = resp.json()
        ok_cookie = 0
        for cookie in self.session.cookies:
            if cookie.name == 'var1' and cookie.value == '1':
                ok_cookie += 1
            if cookie.name == 'var2' and cookie.value == 'a':
                ok_cookie += 1
        self.assertEqual(ok_cookie, 2)

        url = 'http://httpbin.org/get'
        http_get = URLFetch(url=url, session=self.session)
        try:
            resp = http_get(key1='val1', key2='val2')
        except requests.exceptions.ConnectionError as e:
            raise requests.exceptions.ConnectionError('Error fetching (check proxy settings):',url)
        rjson = resp.json()
        self.assertGreaterEqual(rjson['headers']['Cookie'].find('var1=1'),0)
        
    def test_headers(self):
        url = 'http://httpbin.org/get'
        http_get = URLFetch(url=url, session=self.session)
        try:
            resp = http_get(key1='val1', key2='val2')
        except requests.exceptions.ConnectionError as e:
            raise requests.exceptions.ConnectionError('Error fetching (check proxy settings):',url)
        json = resp.json()
        self.assertEqual(json['headers']['Host'], 'httpbin.org')
        self.assertEqual(json['headers']['User-Agent'], 'Testing')
        
if __name__ == '__main__':
    #unittest.main()

    suite = unittest.TestLoader().loadTestsFromTestCase(TestCommons)
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
        
