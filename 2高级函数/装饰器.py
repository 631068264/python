#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'

import functools


def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print 'call %s():' % func.__name__
		return func(*args, **kw)

	return wrapper


@log  # 相当于now = log(now)
def now():
	print '2013-12-25'


now()

print(now.__name__)
