#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2017/4/7 10:49
@annotation = ''
"""


class Base(object):
    base = None

    def run(self):
        print self.base


class A(Base):
    params = None

    def run(self):
        print self.base + self.params

    def __setstate__(self, state):
        print "setstate"
        self.__dict__ = state

    def __getstate__(self):
        print "getstate"
        return self.__dict__

    def __reduce__(self):
        print "reduce"
        return self.__class__, super(A, self).__reduce__(), self.__getstate__()


class B(Base):
    params = None

    def __setstate__(self, state):
        print "setstate"
        self.__dict__ = state

    def __getstate__(self):
        print "getstate"
        return self.__dict__

    def __reduce__(self):
        print "reduce"
        return self.__class__, super(B, self).__reduce__(), self.__getstate__(),

    def run(self):
        print self.base * self.params


def _create(base_class, p):
    class C(base_class):
        params = p

    return C()


def factory(base_class):
    class_list = []
    for i in xrange(0, 500):
        class_list.append(_create(base_class, i))
    return class_list


try:
    import cPickle as pickle
except ImportError:
    import pickle

A_class_list = factory(base_class=A)
B_class_lsit = factory(base_class=B)
for a in A_class_list:
    o = pickle.dumps(a, pickle.HIGHEST_PROTOCOL)
    print o
