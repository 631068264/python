#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'

"""
Python 一切都是对象
"""


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    # private
    def __get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    # 静态方法
    @staticmethod
    def hello(n):
        print(n)


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

# 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性
bart.name = "ajsflasj"
print(bart.name)

# print(bart.get_grade())

Student.hello("uwoerouwoe")
