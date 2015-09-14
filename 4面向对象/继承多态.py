#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'

class Animal(object):
    def run(self):
        print 'Animal is running...'


class Dog(Animal):
    def run(self):
        print 'Dog is running...'

    def eat(self):
        print 'Eating meat...'


class Cat(Animal):
    pass


class Bat(Dog, Cat):
    pass


dog = Dog()
dog.run()

cat = Cat()
cat.run()
