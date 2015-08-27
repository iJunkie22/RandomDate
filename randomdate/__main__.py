__author__ = 'ethan'

from __header__ import *


w_month_int = 1
w_day_int = 1
w_year_int = 1900
w_month_month = Months(w_month_int)

print_date(w_month_month, w_day_int, w_year_int)

w_year_int = get_year()
w_month_int = get_month()
w_day_int = get_day()

w_month_month = Months(w_month_int)

if valid_date(w_month_int, w_day_int, w_year_int):
    print_date(w_month_month, w_day_int, w_year_int)

