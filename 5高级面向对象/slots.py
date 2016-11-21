#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'


class Student(object):
    # 限制class的属性
    #  用tuple定义允许绑定的属性名称
    # 仅对当前类起作用，对继承的子类是不起作用的：
    __slots__ = ('name', 'age')
    pass


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


# Student.set_age = MethodType(set_age, None, Student)  # 给类绑定方法  给对象绑定方法
#
# s = Student()
# s.set_age(45)
# print(s.age)


class A(object):
    def __init__(self, ax, bx):
        self.a = ax
        self.b = bx

    def pr(self):
        print ("dict")

    def __getattr__(self, name):
        print ("__getattr__ %s" % name)

    def __setattr__(self, name, value):
        print ("__setattr__")
        # self.__dict__[name] = value

    def __getattribute__(self, item):
        print ("____getattribute__")

    def __set__(self, instance, value):
        print ("__set__")

    def __get__(self, instance, value):
        print ("__get__")


# a = A(1, 2)
# a.pr()
# a.x
# a.x = 3
# a.f()



class Celsius:
    def __get__(self, instance, owner):
        print ("__get__")
        return 5 * (instance.fahrenheit - 32) / 9.0

    def __set__(self, instance, value):
        print ("__set__")
        instance.fahrenheit = 32


class Temperature:
    celsius = Celsius()

    def __init__(self, initial_f):
        self.fahrenheit = initial_f


t = Temperature(212)
print(t.celsius)
t.celsius = 0
print(t.fahrenheit)
