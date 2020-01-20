import unittest
from nsepy.symbols import get_symbol_list, get_index_constituents_list
import pdb


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

    def test_index_constituents_list(self):
        df = get_index_constituents_list("NIFTY50")
        # Check for 50 items
        self.assertEqual(df.shape[0], 50)

        # Check popular names are in the list
        _sbi = df["Symbol"] == "SBIN"
        # Check company matches the expected value
        self.assertEqual(df[_sbi].iloc[0].get(
            'Company Name'), "State Bank of India")
        self.assertEqual(df[_sbi].iloc[0].get(
            'Industry'), "FINANCIAL SERVICES")

        df = get_index_constituents_list("NIFTYCPSE")
        # Check popular names are in the list
        _oil = df["Symbol"] == "OIL"
        # Check company matches the expected value
        self.assertEqual(df[_oil].iloc[0].get('ISIN Code'), "INE274J01014")
