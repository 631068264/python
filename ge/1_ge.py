# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/8/22 11:52
@annotation = '' 
"""
import gevent


def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')


def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')


# 同时执行或异步执行
gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])
