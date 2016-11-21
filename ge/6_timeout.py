#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/9/17 16:57
@annotation = '' 
"""
# 超时是一种对一块代码或一个Greenlet的运行时间的约束。


import gevent
from gevent import Timeout

seconds = 10

timeout = Timeout(seconds)
timeout.start()


def wait():
    gevent.sleep(10)


try:
    gevent.spawn(wait).join()
except Timeout:
    print('Could not complete')

import gevent
from gevent import Timeout

time_to_wait = 5  # seconds


class TooLong(Exception):
    pass


with Timeout(time_to_wait, TooLong):
    gevent.sleep(10)
