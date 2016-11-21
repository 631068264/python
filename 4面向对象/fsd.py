#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/8/18 15:35
@annotation = '' 
"""


class MetaTable(type):
    def __getattr__(cls, key):
        temp = key.split("__")
        name = temp[0]
        alias = None

        if len(temp) > 1:
            alias = temp[1]

        return cls(name, alias)


class Table(object):
    __metaclass__ = MetaTable

    def __init__(self, name, alias=None):
        self._name = name
        self._alias = alias

    @property
    def show(self):
        print self._name + self._alias


d = Table
d.student__s

args = ('a', 'b')
kwargs = {'kwarg1': True}

