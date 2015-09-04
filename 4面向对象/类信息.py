#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'
import types
# 判断普通的类型
type('abc') == types.StringType
# 对于class的继承关系来说，使用type()就很不方便。
# 我们要判断class的类型，可以使用isinstance()函数。
# object -> Animal -> Dog -> Husky

isinstance('a', (str, unicode))
# isinstance(d, Husky)
"""
类类型
"""

# 可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
dir('ABC')

"""
类长度
"""
# >>> len('ABC')
# 3
# >>> 'ABC'.__len__()
# 3
"""
属性控制
"""
# >>> class MyObject(object):
# ...     def __init__(self):
# ...         self.x = 9
# ...     def power(self):
# ...         return self.x * self.x
# ...
# >>> obj = MyObject()
# >>> hasattr(obj, 'x') # 有属性'x'吗？
# True
# >>> obj.x
# 9
# >>> hasattr(obj, 'y') # 有属性'y'吗？
# False
# >>> setattr(obj, 'y', 19) # 设置一个属性'y'
# >>> hasattr(obj, 'y') # 有属性'y'吗？
# True
# >>> getattr(obj, 'y') # 获取属性'y'
# 19
# >>> obj.y # 获取属性'y'
# 19
# getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404

"""
打印类
"""


class Student(object):
	def __init__(self, name):
		self.name = name

	# 两者的区别是__str__()返回用户看到的字符串，
	# 而__repr__()返回程序开发者看到的字符串，
	# 也就是说，__repr__()是为调试服务的。
	def __str__(self):
		return 'Student object (name=%s)' % self.name

	__repr__ = __str__


s = Student('484')
print(s)

"""
遍历类
"""


# 如果一个类想被用于for ... in循环，类似list或tuple那样，
# 就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环。

class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1  # 初始化两个计数器a，b

	def __iter__(self):
		return self  # 实例本身就是迭代对象，故返回自己

	def next(self):
		self.a, self.b = self.b, self.a + self.b  # 计算下一个值
		if self.a > 100000:  # 退出循环的条件
			raise StopIteration();
		return self.a  # 返回下一个值

	# __setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素
	def __getitem__(self, n):  # 像list那样按照下标取出元素
		a, b = 1, 1
		for x in range(n):
			a, b = b, a + b
		return a


for n in Fib():
	print n
f = Fib()
print(f[5])

"""
只有在没有找到属性的情况下，才调用__getattr__
instance()  任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
"""
