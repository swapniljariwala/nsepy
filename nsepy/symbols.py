import pandas as pd
import io
import re
from nsepy.urls import equity_symbol_list_url, index_constituents_url


def get_symbol_list():
    res = equity_symbol_list_url()
    df = pd.read_csv(io.StringIO(res.content.decode('utf-8')))
    return df


def get_index_constituents_list(index):
    res = index_constituents_url(index.lower())
    df = pd.read_csv(io.StringIO(res.content.decode('utf-8')))
    return df

# def get_index_name(index):
    # p = re.compile(r'^(Nifty)([a-z]*)(\d+)$',re.I )
    # g = list(re.match( p , index).groups())

    # #Remove regex match group that is blank.
    # g.remove('')
    # return ' '.join(g)


def get_index_name(index):
    dctindexname = {
        "INDIAVIX": ["India VIX"],
        # "NIFTY GS 10YR": ["Nifty 10 yr Benchmark G-Sec"],
        # "NIFTY GS 10YR CLN": ["Nifty 10 yr Benchmark G-Sec (Clean Price)"],
        "NIFTY100": ["Nifty 100"],
        # "NIFTY GS 11 15YR": ["Nifty 11-15 yr G-Sec Index"],
        # "NIFTY GS 15YRPLUS": ["Nifty 15 yr and above G-Sec Index"],
        # "": ["Nifty 1D Rate Index"],
        "NIFTY200": ["Nifty 200"],
        # "NIFTY GS 4 8YR": ["Nifty 4-8 yr G-Sec Index"],
        "NIFTY50": ["Nifty 50"],
        # "": ["Nifty 50 Arbitrage"],
        # "": ["Nifty 50 Futures Index"],
        # "": ["Nifty 50 Futures TR Index"],
        "NIFTY500": ["Nifty 500"],
        # "NIFTYGS8TO13YR": ["Nifty 8-13 yr G-Sec"],
        "NIFTYADITYABIRLAGROUP": ["Nifty Aditya Birla Group"],
        "NIFTYALPHA50": ["Nifty Alpha 50"],
        # "": ["NIFTY Alpha Low-Volatility 30"],
        # "": ["NIFTY Alpha Quality Low-Volatility 30"],
        # "": ["NIFTY Alpha Quality Value Low-Volatility 30"],
        "NIFTYAUTO": ["Nifty Auto"],
        "NIFTYBANK": ["Nifty Bank"],
        "NIFTYCOMMODITIES": ["Nifty Commodities"],
        "NIFTYGSCOMPOSITE": ["Nifty Composite G-sec Index"],
        "NIFTYCONSUMERDURABLES": ["Nifty Consumer Durables"],
        "NIFTYCPSE": ["Nifty CPSE"],
        "NIFTYDIVOPP50": ["Nifty Dividend Opportunities 50"],
        "NIFTYENERGY": ["Nifty Energy"],
        "NIFTYFINANCE": ["Nifty Financial Services"],
        "NIFTYFMCG": ["Nifty FMCG"],
        # "": ["Nifty Free Float Midcap 100"],
        # "": ["Nifty Free Float Smallcap 100"],
        # "": ["Nifty Full Midcap 100"],
        # "": ["Nifty Full Smallcap 100"],
        "NIFTY GROWSECT 15": ["Nifty Growth Sectors 15"],
        # "": ["Nifty High Beta 50"],
        "NIFTYCONSUMPTION": ["Nifty India Consumption"],
        "NIFTYINFRA": ["Nifty Infrastructure"],
        "NIFTYIT": ["Nifty IT"],
        "NIFTYLARGEMIDCAP250": ["Nifty LargeMidcap 250"],
        # "": ["Nifty Low Volatility 50"],
        # "": ["Nifty Mahindra Group"],
        "NIFTYMEDIA": ["Nifty Media"],
        "NIFTYMETAL": ["Nifty Metal"],
        "NIFTYMIDCAP100": ["Nifty Midcap 100"],
        "NIFTYMIDCAP150": ["Nifty Midcap 150"],
        "NIFTYMIDCAP50": ["Nifty Midcap 50"],
        "NIFTY_MIDCAP_LIQUID15": ["Nifty Midcap Liquid 15"],
        "NIFTYMIDSMALLCAP400": ["Nifty MidSmallcap 400"],
        "NIFTYMNC": ["Nifty MNC"],
        "NIFTYNEXT50": ["Nifty Next 50"],
        "NIFTYOILGAS": ["Nifty Oil & Gas"],
        "NIFTYPHARMA": ["Nifty Pharma"],
        "NIFTYPVTBANK": ["Nifty Private Bank"],
        "NIFTYPSE": ["Nifty PSE"],
        "NIFTYPSUBANK": ["Nifty PSU Bank"],
        # "": ["Nifty Quality 30"],
        # "": ["NIFTY Quality Low-Volatility 30"],
        "NIFTYREALTY": ["Nifty Realty"],
        "NIFTYSERVSECTOR": ["Nifty Services Sector"],
        # "": ["Nifty Shariah 25"],
        "NIFTYSMALLCAP100": ["Nifty Smallcap 100"],
        "NIFTYSMALLCAP250": ["Nifty Smallcap 250"],
        "NIFTYSMALLCAP50": ["Nifty Smallcap 50"],
        # "": ["NIFTY SME EMERGE"],
        # "": ["Nifty Tata Group"],
        # "": ["Nifty Tata Group 25% Cap"],
        # "": ["NIFTY100 Alpha 30"],
        # "": ["NIFTY100 Enhanced ESG"],
        "NIFTY100EQUALWEIGHT": ["Nifty100 Equal Weight"],
        # "": ["NIFTY100 ESG"],
        "NIFTY_MIDCAP_LIQUID15": ["Nifty100 Liquid 15"],
        "NIFTY100LOWVOLATILITY30": ["Nifty100 Low Volatility 30"],
        "NIFTY100QUALITY30": ["NIFTY100 Quality 30"],
        # "NIFTY200QUALITY30": ["NIFTY200 Quality 30"],
        # "NIFTY50DIVPOINT": ["Nifty50 Dividend Points"],
        "NIFTY50EQUALWEIGHT": ["NIFTY50 Equal Weight"],
        # "NIFTY50 PR 1X INV": ["Nifty50 PR 1x Inverse"],
        # "NIFTY50 PR 2X LEV": ["Nifty50 PR 2x Leverage"],
        # "": ["Nifty50 Shariah"],
        # "NIFTY50 TR 1X INV": ["Nifty50 TR 1x Inverse"],
        # "NIFTY50 TR 2X LEV": ["Nifty50 TR 2x Leverage"],
        # "": ["Nifty50 USD"],
        "NIFTY50_VALUE20": ["Nifty50 Value 20"],
        # "": ["Nifty500 Shariah"],
        # "NIFTY500_VALUE50": ["NIFTY500 Value 50"],
    }

    df = pd.DataFrame.from_dict(dctindexname, orient='index', columns=["Name"])
    dfret = df.loc[df.index == index]
    return dfret['Name'][0]
