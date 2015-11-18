# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 23:56:19 2015

@author: jerry
"""


NSE_INDICES = ["NIFTY 50",
               "NIFTY NEXT 50",
               "NIFTY100 LIQ 15",
               "NIFTY 100",
               "NIFTY 200",
               "NIFTY 500",
               "NIFTY MIDCAP 50",
               "NIFTY MIDCAP 100",
               "NIFTY SMALL 100",
               "NIFTY AUTO",
               "NIFTY BANK",
               "NIFTY ENERGY",
               "NIFTY FIN SERVICE",
               "NIFTY FMCG",
               "NIFTY IT",
               "NIFTY MEDIA",
               "NIFTY METAL",
               "NIFTY PHARMA",
               "NIFTY PSU BANK",
               "NIFTY REALTY",
               "NIFTY COMMODITIES",
               "NIFTY CONSUMPTION",
               "NIFTY CPSE",
               "NIFTY INFRA",
               "NIFTY MNC",
               "NIFTY PSE",
               "NIFTY SERV SECTOR",
               "NIFTY SHARIAH 25",
               "NIFTY50 SHARIAH",
               "NIFTY500 SHARIAH",
               "NIFTY100 EQUAL WEIGHT",
               "NIFTY50 USD",
               "NIFTY50 DIV POINT",
               "NIFTY DIV OPPS 50",
               "NIFTY ALPHA 50",
               "NIFTY HIGH BETA 50",
               "NIFTY LOW VOLATILITY 50",
               "NIFTY QUALITY 30",
               "NIFTY50 VALUE 20",
               "NIFTY GROWSECT 15",
               "NIFTY50 TR 2X LEV",
               "NIFTY50 TR 1X INV",               
               ]

DERIVATIVE_TO_INDEX = {"NIFTY": "NIFTY 50",
               "BANKNIFTY": "NIFTY BANK",
               "NIFTYINFRA": "NIFTY INFRA",
               "NIFTYIT": "NIFTY IT",
               "NIFTYMID50": "NIFTY MIDCAP 50",
               "NIFTYPSE": "NIFTY PSE"}

INDEX_DERIVATIVES = DERIVATIVE_TO_INDEX.keys()
INDEX_DERIVATIVES.append('S&P500')
INDEX_DERIVATIVES.append('DJIA')
INDEX_DERIVATIVES.append('FTSE100')