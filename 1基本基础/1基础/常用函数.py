#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L = range(100)
print(L[:3])  # 有0开始 3 不包括3

print(L[::5])  # 每5个取一个

print(L[:])  # 复制一个

print(L[::-1])  # 逆序
# 迭代
d = {'a': 1, 'b': 2, 'c': 3}  # 一般迭代key
for value in d.itervalues():  # for k, v in d.iteritems()
    print(value)

for i, value in enumerate(['A', 'B', 'C']):  # enumerate函数可以把一个list变成索引-元素对
    print i, value

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y
# 列表生成式
range(1, 11)  # 1 -10

L = []
for x in range(1, 11):
    L.append(x * x)
[x * x for x in range(1, 11)]

[x * x for x in range(1, 11) if x % 2 == 0]

[m + n for m in 'ABC' for n in 'XYZ']

print("x" + "y")

"""
按照某种算法推算出来
在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间
生成器（Generator）[] ==>()
"""
g = (x * x for x in range(10))


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1


"""
generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
"""


def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
