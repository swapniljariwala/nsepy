

import datetime
from datetime import date
import re

from nsepy import urls

re_date = re.compile("([0-9]{2}\-[0-9]{2}\-[0-9]{4})")
idx_exp = {}
vix_exp = {}
stk_exp = {}


def add_dt(instru, dt):
    if not dt.year in instru:
        instru[dt.year] = {}

    if not dt.month in instru[dt.year]:
        instru[dt.year][dt.month] = set()

    instru[dt.year][dt.month].add(dt)


class ExpiryDateError(Exception):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super(ExpiryDateError, self).__init__(message)


def build_dt_dict():
    lines = urls.derivative_expiry_dates_url().text

    for line in lines.split('\n'):
        s = re_date.search(line)

        if s:
            dt = datetime.datetime.strptime(s.group(1), "%d-%m-%Y").date()
            # Start Kludge
            # The list on NSE portal for expiry date has a wrong entry for 20 Sep 2019
            # Handle this oulier use case by ignoring this date and skpping it for processing
            if dt == datetime.datetime(2019, 9, 20).date():
                continue
            # End Kludge
            if line.find('indxExpryDt') > -1:
                try:
                    existing_date = try_to_get_expiry_date(
                        dt.year, dt.month, index=True)
                    if existing_date < dt:
                        add_dt(idx_exp, dt)
                except:
                    add_dt(idx_exp, dt)

            if line.find('stk') > -1:
                try:
                    existing_date = try_to_get_expiry_date(
                        dt.year, dt.month, index=False, stock=False, vix=False)
                    if existing_date < dt:
                        add_dt(stk_exp, dt)
                except:
                    add_dt(stk_exp, dt)

            if line.find('vix') > -1:
                try:
                    existing_date = try_to_get_expiry_date(
                        dt.year, dt.month, index=False, stock=False, vix=True)
                    if existing_date < dt:
                        add_dt(vix_exp, dt)
                except:
                    add_dt(vix_exp, dt)


def is_valid_expiry(dt):
    # not a perfect logic :P
    if (dt.month != 2 and dt.day >= 23) or (dt.month == 2 and dt.day >= 21):
        return True


def try_to_get_expiry_date(year, month, index=True, stock=False, vix=False):

    try:
        if vix and vix_exp:
            return vix_exp[year][month]

        if stock and stk_exp:
            return stk_exp[year][month]

        if index and idx_exp:
            return idx_exp[year][month]

        raise Exception
    except:

        if index:
            name = 'index derivatives'
        if stock:
            name = 'stock derivatives'
        else:
            name = 'vix derivatives'
        raise ExpiryDateError(
            'No expiry date found in the month of {}-{} for {}'.format(year, month, name))


def get_expiry_date(year, month, index=True, stock=False, vix=False, recursion=0):

    try:
        return try_to_get_expiry_date(year, month, index, stock, vix)
    except:

        if recursion > 1:
            raise

        else:
            pass

    #print("building dictionary")

    build_dt_dict()
    return get_expiry_date(year, month, index, stock, vix, recursion=recursion+1)
