#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/9/17 18:04
@annotation = '' 
"""


# 组(group)是一个运行中greenlet的集合，集合中的greenlet像一个组一样 会被共同管理和调度。
# 它也兼饰了像Python的multiprocessing库那样的 平行调度器的角色。
from greenlet import getcurrent

import gevent
from gevent.pool import Group
#
#
# def talk(msg):
#     for i in xrange(3):
#         gevent.sleep(0)
#         print(msg)
#
#
# g1 = gevent.spawn(talk, 'bar')
# g2 = gevent.spawn(talk, 'foo')
# g3 = gevent.spawn(talk, 'fizz')
#
# group = Group()
# group.add(g2)
# group.join()
#
# group.add(g3)
# group.add(g1)
# group.join()




group = Group()


# def hello_from(n):
#     print('Size of group %s' % len(group))
#     print('Hello from Greenlet %s' % id(getcurrent()))
#     return id(getcurrent())
#
# o = group.map(hello_from, xrange(3))
# print o


# def intensive(n):
#     gevent.sleep(3 - n)
#     return 'task', n
#
#
# print('Ordered')
#
# ogroup = Group()
# for i in ogroup.imap(intensive, xrange(3)):
#     print(i)
#
# print('Unordered')
#
# igroup = Group()
# for i in igroup.imap_unordered(intensive, xrange(3)):
#     print(i)
