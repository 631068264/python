#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/6 21:51
@annotation = '' 
"""
city = {
    "available": [1, 2]
}
c = lambda v: (v in city["available"], v)
print c(1)

import calendar
from datetime import date, timedelta


def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)


print get_month_range()
