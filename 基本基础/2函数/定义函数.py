#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'
"""
自定义函数 检查参数个数 不会检查参数类型
"""


def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x


print(my_abs(-4546446.456454))
print(my_abs('A'))


# 空函数
def nop():
	pass


# 参数检查
def my_abs1(x):
	if not isinstance(x, (int, float)):  # x可以是int float
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x


# print(my_abs1('A')) #会报错

# 返回多个值
import math


def move(x, y, step, angle=0):  # 参数有默认值 调用时可以不写该参数
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny


"""
原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，
而多个变量可以同时接收一个tuple，按位置赋给对应的值，
所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
"""
x, y = move(100, 100, 60, 86)  # 返回
print x, y

x = move(100, 100, 60, 86)  # 返回
print x

"""
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，
默认参数的内容就变了，不再是函数定义时的[]了。

所以，定义默认参数要牢记一点：默认参数必须指向不变对象！

因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。
我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
"""


def add_end(L=None):  # L []
	if L is None:
		L = []
	L.append('END')
	return L


def add_end1(K=[]):  # L []
	if K is None:
		K = []
	K.append('END')
	return K


print(add_end1([1, 2]))
print(add_end1([1, 2]))
print(add_end1())
print(add_end1())


# 可变参数
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum


nums = [1, 2, 3]
print(calc(*nums))


# 可选参数
def person(name, age, **kw):
	print 'name:', name, 'age:', age, 'other:', kw


print(person('Michael', 30))
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw)

"""
必选参数、默认参数、可变参数和关键字参数

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。
"""
