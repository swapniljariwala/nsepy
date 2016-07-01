import archives

import datetime
from datetime import date
import re

from nsepy import urls

re_date = re.compile("([0-9]{2}\-[0-9]{2}\-[0-9]{4})")
idx_exp = {}
vix_exp = {}
stk_exp = {}

def add_dt(instru, dt):
	try:
		instru[dt.year][dt.month] = dt
	except:
		instru[dt.year]={}
		instru[dt.year][dt.month] = dt

class ExpiryDateError(Exception):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super(ExpiryDateError, self).__init__(message)

		
def build_dt_dict():
	lines = urls.derivative_expiry_dates_url().text
	
	for line in lines.split('\n'):
		s =  re_date.search(line)
		if s:
			dt = datetime.datetime.strptime(s.group(1), "%d-%m-%Y").date()
			if line.find('indxExpryDt')>-1:
				add_dt(idx_exp, dt)
			if line.find('stk')>-1:
				add_dt(stk_exp, dt)
			if line.find('vix')>-1:
				add_dt(vix_exp, dt)
		
def get_expiry_date(year, month, index=True, stock=False, vix=False):
	
	try:
		raise Exception
		if vix and vix_exp:
			return vix_exp[year][month]
		
		if stock and stk_exp:
			return stk_exp[year][month]

		
		if index and idx_exp:
			return idx_exp[year][month]
	except:
		print 'except'
		if index:
			name = 'index derivatives'
		if stock:
			name = 'stock derivatives'
		else:
			name = 'vix derivatives'
		raise ExpiryDateError('No expiry date found in the month of {}-{} for {}'.format(year, month, name))
	print("building dict")

	build_dt_dict()
	return get_expiry_date(year, month, index, stock, vix)
