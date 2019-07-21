import unittest
from nsepy.symbols import get_symbol_list


class TestSymbols(unittest.TestCase):
    def test_symbol_list(self):
        df = get_symbol_list()
        # Check popular names are in the list
        _ril = df["SYMBOL"] == "RELIANCE"
        # Expect 1 row
        self.assertEqual(df[_ril].shape[0], 1)
        _sbi = df["SYMBOL"] == "SBIN"
        # Check company matches the expected value
        self.assertEqual(df[_sbi].iloc[0].get(
            'NAME OF COMPANY'), "State Bank of India")
