from nsepy.commons import (is_index, is_index_derivative, 
                           NSE_INDICES, INDEX_DERIVATIVE,
                           ParseTables, StrDate)
                           
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
    for i in range(0, len(lists)):
        for j in range(0, len(lists[i])):
            lists[i][j] = schema[i](lists[i][j])
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
        # test equity tables
        dd_mmm_yyyy = StrDate.default_format(format = "%d-%b-%Y")
        #schema for equity history values
        schema = [str, str,
                  dd_mmm_yyyy,
                  float, float, float, float,
                  float, float, float, int, float,
                  int, int, float ]
        bs = BeautifulSoup(htmls.html_equity)
        t = ParseTables(soup=bs,
                        schema = schema)
                        
        lst = text_to_list(htmls.csv_equity, schema)
        self.assertEqual(lst, t.get_tables())
        
        #test derivative tables
        
        #test index tables
    
    def test_StrDate(self):
        dd_mmm_yyyy = StrDate.default_format(format = "%d-%b-%Y")
        dt1 = dd_mmm_yyyy(string = "12-Nov-2012")
        dt2 = datetime.date(2012,11,12)
        self.assertEqual(dt1, dt2)
        
        
        
    

if __name__ == '__main__':
    unittest.main()
    
    

