#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'

"""
Python 一切都是对象
"""


class Student(object):
    def __init__(self, name, score):
        self.__name = name  # 私有变量
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__get_grade())

    # private
    def __get_grade(self):  # 私有方法
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    @classmethod
    def class_func(cls):
        """ 定义类方法，至少有一个cls参数 """

        print '类方法'

    @staticmethod
    def static_func():
        """ 定义静态方法 ，无默认参数"""

        print '静态方法'


bart = Student('Bart Simpson', 59)
bbrt = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print bart == bbrt
bart.print_score()
lisa.print_score()

# 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性
bart.name = "ajsflasj"
print(bart.name)

fuck = Student()
fuck.class_func()
fuck.static_func()

Fuck.class_func()
Fuck.static_func()
