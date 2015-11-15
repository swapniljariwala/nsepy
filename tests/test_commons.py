from nsepy.commons import (is_index, is_index_derivative, 
                           NSE_INDICES, INDEX_DERIVATIVE,
                           ParseTables)
                           
import datetime
import unittest
from bs4 import BeautifulSoup
from tests import htmls
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
        
        
        
    

if __name__ == '__main__':
    unittest.main()
    
    

