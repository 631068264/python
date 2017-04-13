#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2017/4/13 21:32
@annotation = ''
"""
import inspect


def func(a, b=1, *args, **kwargs):
    b = 4
    print b


sf = inspect.getcallargs(func, 1, 2, 4, 234, p=4)
print sf

print getattr(func, "b", None)
