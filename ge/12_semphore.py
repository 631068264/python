#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/8/22 15:27
@annotation = '' 
"""
from gevent import sleep
from gevent.coros import BoundedSemaphore
from gevent.pool import Pool

sem = BoundedSemaphore(2)


def worker1(n):
    sem.acquire()
    print('Worker %i acquired semaphore' % n)
    sleep(0)
    sem.release()
    print('Worker %i released semaphore' % n)


def worker2(n):
    with sem:
        print('Worker %i acquired semaphore' % n)
        sleep(0)
    print('Worker %i released semaphore' % n)


pool = Pool()
pool.map(worker1, xrange(0, 3))
pool.map(worker2, xrange(3, 6))
