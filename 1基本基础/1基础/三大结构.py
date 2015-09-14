#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'

"""
判断结构
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
"""
age = 20
if age < 18:
    print(age)
else:
    print(age + 1)
# safe_vars.trade_category = "" if company.trade_category is None else company.trade_category
"""
循环
"""
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

sum = 0
for x in range(101):
    sum = sum + x
print sum
"""
循环 while
"""
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum
