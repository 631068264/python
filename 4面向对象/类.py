#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'

"""
Python 一切都是对象
"""


class Student(object):
    age = 89

    def __init__(self, name):
        self.__name = name  # 私有变量
        self.__score = "89"

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
        print cls.age
        print '类方法'

    @staticmethod
    def static_func():
        """ 定义静态方法 ，无默认参数"""
        print Student.age
        print '静态方法'


bart = Student('Bart Simpson')
bbrt = Student('Bart Simpson')
lisa = Student('Lisa Simpson')
print bart == bbrt
bart.print_score()
lisa.print_score()

Student.class_func()
Student.static_func()


# 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性
# bart.name = "ajsflasj"
# print(bart.name)

# fuck = Student()
# fuck.class_func()
# fuck.static_func()
#
# Student.class_func()
# Student.static_func()
