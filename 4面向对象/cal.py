#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/4 14:16
@annotation = '' 
"""


# class Call(object):
#     def __init__(self):
#         print "init"
#
#     def __call__(self, *args, **kwargs):
#         print "call"
#
#
# call = Call()
# call()
# assert callable(call)


#######################################
class One(object):
    def __init__(self):
        self.value *= 2


class Two(object):
    def __init__(self):
        self.value += 5


class Base(object):
    def __init__(self, value):
        self.value = value


class Child(Base):
    def __init__(self, value):
        Base.__init__(self, 5)


# (5*2)+5 与继承顺序有关
class OneWay(Child, One, Two):
    def __init__(self, value):
        Child.__init__(self, value)
        One.__init__(self)
        Two.__init__(self)


print OneWay(5).value
