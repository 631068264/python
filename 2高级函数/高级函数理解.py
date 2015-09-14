#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'
"""
函数可赋值 作为变量 和参数
"""
f = abs
print(f(-79.555))


# 高阶函数
def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))


# map(函数,序列) 分别算
# reduce(函数,序列) 合起算

def not_empty(s):
    return s and s.strip()


filter(not_empty, ['A', '', 'B', None, 'C', '  '])


# 倒序
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0


# 忽略大小写
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0


sorted([36, 5, 12, 9, 21], reversed_cmp)


# 返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j

            return g

        fs.append(f(i))
    return fs


f1, f2, f3 = count()

# 匿名函数
map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# def f(x):
#     return x * x
