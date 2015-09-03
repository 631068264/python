#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'
def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)


def fact(n):
	return fact_iter(n, 1)


def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)


"""
使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
"""
