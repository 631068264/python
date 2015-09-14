#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'

from types import MethodType


class Student(object):
    # 限制class的属性
    #  用tuple定义允许绑定的属性名称
    # 仅对当前类起作用，对继承的子类是不起作用的：
    __slots__ = ('name', 'age')
    pass


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


Student.set_age = MethodType(set_age, None, Student)  # 给类绑定方法  给对象绑定方法

s = Student()
s.set_age(45)
print(s.age)
