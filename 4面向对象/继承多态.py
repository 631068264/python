#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'

class Animal(object):
    def __init__(self):
        print '__init__Animal'

    def run(self):
        print 'Animal is running...'


class Dog(Animal):
    def __init__(self):
        print '__init__Dog'

    def run(self):
        print 'Dog is running...'


class Cat(Animal):
    def __init__(self, s, *args, **kwargs):
        print s
        print '__init__Cat'

    def run(self):
        print 'Cat is running...s'


class Bat(Cat, Dog):
    """
    父类继承object 子类继承的方法按广度优先
    """

    def __init__(self, s):
        super(Bat, self).__init__(s)

    def sdf(self):
        super(Bat, self).run()
        self.run()
        # Dog.run(self)

    def f(self):
        # Dog.__init__(self)
        pass


class Fuck(Cat, Dog):
    @classmethod
    def class_func(cls):
        """ 定义类方法，至少有一个cls参数 """

        print '类方法'

    @staticmethod
    def static_func():
        """ 定义静态方法 ，无默认参数"""

        print '静态方法'


bat = Bat("df")
bat.sdf()
# bat.run()
# bat.sdf()

# fuck = Fuck()
# fuck.class_func()
# fuck.static_func()
#
# Fuck.class_func()
# Fuck.static_func()
