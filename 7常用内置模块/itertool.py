#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'
"""
count()会创建一个无限的迭代器，打印出自然数序列
cycle()会把传入的一个 序列 无限重复下去
repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
"""

import itertools

natuals = itertools.count(1)
for n in natuals:
	print n


# 无限序列虽然可以无限迭代下去，
# 通过takewhile()等函数根据条件判断来截取出一个有限的序列：
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
	print n

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
	print c
