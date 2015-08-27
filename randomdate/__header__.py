__author__ = 'ethan'

import random
import time
import calendar
from sys import stderr


#################################################
# Stuff to make it behave more like C++
#################################################


def strict_types(*deco_args):
    def decorator(child_func):
        def wrapped(*child_args):
            assert len(deco_args) == len(child_args)
            for i, o, t in zip(range(len(child_args)), child_args, deco_args):
                try:
                    assert isinstance(o, t)
                except AssertionError as _ae:
                    stderr.write("{} (Argument {} of {}) is not of type {}\n".
                                 format(repr(o), i, child_func.__name__, t.__name__))
                    raise Exception(_ae)
            return child_func(*child_args)
        return wrapped
    return decorator

#################################################
# Months class that replaces the C++ Months enum
#################################################


class Months(int):
    @property
    def is_valid(self):
        return 0 < int(self) < 13

    @property
    def str_abbr(self):
        if not self.is_valid:
            return None
        else:
            return calendar.month_abbr[self].upper()

    @property
    def str_long(self):
        if not self.is_valid:
            return None
        else:
            return calendar.month_name[self].title()

#################################################
# Stuff for seeding and using random
#################################################


seeded = False
rand = random.Random()


@strict_types(bool)
def set_seeded(bool_value):
    global seeded
    seeded = bool_value


def get_seeded():
    global seeded
    return seeded


def seed_rand():
    result = time.time()
    time_int = int(result * 10000)
    global rand
    rand.seed(time_int)
    set_seeded(True)


def needs_seed(child_function):
    def func_wrapper():
        if not get_seeded():
            seed_rand()
        return child_function()
    return func_wrapper


#################################################
# Functions that in C++ would go in functs.cpp
#################################################


@needs_seed
def get_year():
    return int(rand.random() * 1000000) % 101 + 1900
    # End of get_year


@needs_seed
def get_month():
    return int(rand.random() * 1000000) % 12 + 1
    # End of get_month


@needs_seed
def get_day():
    return int(rand.random() * 1000000) % 31 + 1
    # End of get_day


@strict_types(int, int, int)
def valid_date(month, day, year):
    month_m = Months(month)

    if not 1900 <= year <= 2001:
        return False
    elif not 1 <= month <= 12:
        return False
    elif not 1 <= day <= 31:
        return False
    elif day == 31 and month_m.str_abbr in ['APR', 'JUN', 'SEP', 'NOV']:
        return False
    elif month == 2 and day > 28:
        return False
    return True
    # End of valid_date


@strict_types(Months, int, int)
def print_date(o_month, o_day, o_year):
    if o_month.is_valid:
        print("{} {}, {}".format(o_month.str_long, o_day, o_year))
    else:
        print("invalid month")
