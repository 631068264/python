#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/4 14:16
@annotation = '' 
"""


# class Base(object):
#     def __init__(self, value):
#         self.value = value
#
#
# class Child(Base):
#     def __init__(self, value):
#         Base.__init__(self, 5)
#
#
# class One(Child):
#     def __init__(self, value):
#         Child.__init__(self, value)
#         self.value *= 2
#
#
# class Two(Child):
#     def __init__(self, value):
#         Child.__init__(self, value)
#         self.value += 5
#
#
# # (5*2)+5 与继承顺序有关
# class OneWay(One, Two):
#     def __init__(self, value):
#         One.__init__(self, value)
#         Two.__init__(self, value)
#
#
# print OneWay(5).value


#################################3##3#


class Base(object):
    def __init__(self, value):
        self.value = value


class Child(Base):
    def __init__(self, value):
        Base.__init__(self, value)


class One(Child):
    def __init__(self, value):
        super(One, self).__init__(value)
        self.value *= 2


class Two(Child):
    def __init__(self, value):
        super(Two, self).__init__(value)
        self.value += 5


# (5*2)+5 与继承顺序有关
class OneWay(One, Two):
    def __init__(self, value):
        super(OneWay, self).__init__(value)


print OneWay.mro()
print OneWay(5).value
