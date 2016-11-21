#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'

def gen(max):
    i = 0
    while i < max:
        yield i
        i += 1


for x in gen(10):
    print x
