#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2017/10/9 11:16
@annotation = ''
"""
from __future__ import division

import copy

"""
用不同方法读写同一个内存
内容字节不会随便移动
"""
count = 0
total = 0


def make_avg():
    def __call__():
        print u"fadfdfaf呜呜呜呜"

    def avg(num):
        global count
        global total
        count += 1
        total += num
        print count, total
        return float(total / count)

    return avg


if False:
    avg = make_avg()
    print avg(10)
    print avg(5)
    print avg(3)
    print avg(1)

l1 = [3, [2, 55], [10, 11]]
l2 = copy.deepcopy(l1)
l1.append(100)
l1[1].remove(55)
print l1
print l2
l2[1] += [33, 22]
l2[2] += [33, 22]
print l1
print l2
