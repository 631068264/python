#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2017/4/7 10:49
@annotation = ''
"""


class Base(object):
    def __init__(self):
        self.base = None

    def run(self):
        print self.base


class A(Base):
    def __init__(self, params):
        self.params = params
        super(A, self).__init__()

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
    def __init__(self, params):
        self.params = params
        super(B, self).__init__()

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


class C(object):
    def __init__(self, path):
        self.path = path

    @classmethod
    def get(cls, path):
        return cls(path)


def _create(base_class, p):
    return base_class(params=p)


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
    # print o

# from ctypes import py_object, pythonapi
#
# mappingproxy = pythonapi.PyDictProxy_New
# mappingproxy.argtypes = [py_object]
# mappingproxy.restype = py_object
#
# bundle = {}
# b = mappingproxy(bundle)
# bundle["sdf"] = 1
# print b
