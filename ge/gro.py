#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/8/22 14:57
@annotation = '' 
"""
import gevent
from gevent.pool import Group


def talk(msg):
    for i in xrange(3):
        print(msg)
    return msg

g1 = gevent.spawn(talk, 'bar')
g2 = gevent.spawn(talk, 'foo')
g3 = gevent.spawn(talk, 'fizz')

group = Group()
group.add(g1)
group.join()

group.add(g3)
group.add(g2)
group.join()

import gevent
from gevent.pool import Group


# group = Group()
#
#
# def hello_from(n):
#     print('Size of group %s' % len(group))
#     print('Hello from Greenlet %s' % id(getcurrent()))
#
#
# group.map(hello_from, xrange(3))


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



# print('Unordered')
#
# igroup = Group()
# for i in igroup.imap_unordered(intensive, xrange(3)):
#     print(i)
