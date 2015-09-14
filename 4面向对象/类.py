#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def __get_grade(self):  # private
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

# 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性
bart.name = "ajsflasj"
print(bart.name)

print(bart.get_grade())
