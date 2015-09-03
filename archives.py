# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 09:07:27 2015

@author: swapnil jariwala
"""
#import numpy as np
import requests as req
import datetime
NSE_URL = 'http://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?symbol=sbin&segmentLink=3&symbolCount=1&series=EQ&dateRange=+&fromDate=01-08-2015&toDate=30-09-2015&dataType=PRICEVOLUMEDELIVERABLE'
NSE_CSV = 'http://www.nseindia.com/content/equities/scripvol/datafiles/'



def __get_archive_data_raw(stock, start, end):
    url = NSE_CSV + date_to_str(start) + "-TO-" + date_to_str(end) + stock + "EQN.csv"
    resp = req.get(url)
    #print resp.request.url
    if resp.status_code == 404:
        raise ValueError, 'NSE denied data, try after sometime\n' + resp.request.url
    return resp.text

def stock_history(stock, start, end, output):
    text = __get_archive_data_raw(stock, start, end)
    with open(output, 'w') as f:
        f.write(text)
    
def date_to_str(d):    
    return str(d.day).zfill(2) + '-' + str(d.month).zfill(2) + '-' + str(d.year).zfill(2)

end = datetime.date.today() - datetime.timedelta(1)
dt = datetime.timedelta(6)

start = end - dt

from nselist import nse_to_icici
count_success = 0
count_fail = 0
count_unknown = 0
ok = 0
with open('output.csv','w') as op:
    for d in nse_to_icici.keys():
        try:
            end = datetime.date.today() - datetime.timedelta(1)
            start = end - datetime.timedelta(6)
            __get_archive_data_raw(d.replace('-EQ',''), start, end)
            ok = 0
        except ValueError as e:           
            ok = 1
        except KeyboardInterrupt:
            print 'ok bye'
            break
        except: ok = 2

        if ok == 0: count_success += 1
        elif ok == 1: count_fail += 1
        else: count_unknown += 1
        text = d + ',' + str(ok) + '\n'
        #print d + ' '  + str(ok) + ' ' + str(count_success)  + ' ' + str(count_success + count_fail + count_unknown)
        op.write(text)
        
