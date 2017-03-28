#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/9/17 19:11
@annotation = '' 
"""
# 池(pool)是一个为处理数量变化并且需要限制并发的greenlet而设计的结构。
# 在需要并行地做很多受限于网络和IO的任务时常常需要用到它。


from gevent.pool import Pool

pool = Pool(2)


def hello_from(n):
    print('Size of pool %s' % len(pool))
    return len(pool)

p = pool.map(hello_from, xrange(3))
print p
