#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2017/6/13 10:08
@annotation = ''
"""
import weakref


class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]


def create():
    for cheese in catalog:
        stock[cheese.kind] = cheese


create()
print sorted(stock.keys())
del catalog
print sorted(stock.keys())
# del cheese
# sorted(stock.keys())
