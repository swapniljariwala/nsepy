# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:33:20 2015

@author: SW274998
"""
from nsepy.archives import get_price_history
from datetime import date
import numpy
start = date(2010,6,1)
end = date(2015,9,1)

d = get_price_history(stock = 'RELIANCE',start = start, end = end)
d['VLog'] = numpy.log10(d['Volume'])
d['Ratio'] = d['High'] /d['Low'] - 1
d[[ 'Ratio','VLog']].plot(secondary_y = 'VLog')
