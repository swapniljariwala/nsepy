from nsepy.commons import (is_index, is_index_derivative, 
                           NSE_INDICES, INDEX_DERIVATIVE,
                           ParseTables)
                           
import datetime
import unittest
from bs4 import BeautifulSoup
from tests import htmls

def text_to_list(text, schema):
    rows = text.split('\n')
    lists = []
    for row in rows:
        if not row:
            continue
        cols = row.split(',')
        i = 0
        for cell in cols:
            try:
                lists[i].append(cell)
            except:
                lists.append([])
                lists[i].append(cell)
            i += 1
    return lists  
class TestCommons(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_is_index(self):
        for i in NSE_INDICES:
            self.assertTrue(is_index(i))
    
    def test_is_index_derivative(self):
        for i in INDEX_DERIVATIVE.keys():
            self.assertTrue(is_index_derivative(i))
    
    def test_ParseTables_equity(self):
        schema = [str, str,
                  datetime.date,
                  float, float, float, float,
                  float, float, float, int, float,
                  int, int, float ]
        bs = BeautifulSoup(htmls.html_equity)
        t = ParseTables(soup=bs,
                        schema = schema)
        
        
        
    

if __name__ == '__main__':
    unittest.main()
    
    

