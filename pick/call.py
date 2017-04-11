#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2017/4/7 11:00
@annotation = ''
"""
try:
    import cPickle as pickle
except ImportError:  # pragma: nocover
    import pickle
from pick.base import create, A

class_list = create(base_class=A)

for c in class_list:
    o = pickle.dumps(c, pickle.HIGHEST_PROTOCOL)
    print o
