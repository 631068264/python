#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'

class Animal(object):
    def run(self):
        print 'Animal is running...'


class Dog(Animal):
    def run(self):
        print 'Dog is running...'


class Cat(Animal):
    def run(self):
        print 'Cat is running...'


class Bat(Cat, Dog):
    """
    父类继承object 子类继承的方法按广度优先
    """

    def sdf(self):
        super(Dog, self).run()
        Dog.run(self)


class Fuck(Cat, Dog):
    @classmethod
    def class_func(cls):
        """ 定义类方法，至少有一个cls参数 """

        print '类方法'

    @staticmethod
    def static_func():
        """ 定义静态方法 ，无默认参数"""

        print '静态方法'


bat = Bat()
bat.run()
bat.sdf()

fuck = Fuck()
fuck.class_func()
fuck.static_func()

Fuck.class_func()
Fuck.static_func()
