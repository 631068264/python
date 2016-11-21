#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/9/22 10:12
@annotation = ''
"""
from copy import copy, deepcopy


def test():
    def extend_list(val, list=[]):
        list.append(val)
        return list

    list1 = extend_list(10)
    print(list1)
    list2 = extend_list(123, [])
    list3 = extend_list('a')

    print(list1)
    print(list2)
    print(list3)


def deep():
    a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

    b = a  # 赋值，传对象的引用
    c = copy(a)  # 对象拷贝，浅拷贝
    d = deepcopy(a)  # 对象拷贝，深拷贝

    a.append(5)  # 修改对象a
    a[4].append('c')  # 修改对象a中的['a', 'b']数组对象

    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    print('d = ', d)


arr = [[1, 4], [2, 5], [3, 6]]


def getNum(num, data=None):
    while data:
        print(data[0][-1])
        if num > data[0][-1]:
            del data[0]
            print(data)
            getNum(num, data=None)
        elif num < data[0][-1]:
            print(data[0][-1])
            data = list(zip(*data))
            print(data)
            print(data[-1])
            del data[-1]
            data = list(zip(*data))
            print(data)
            getNum(num, data=None)
        else:
            return True
            data.clear()
    return False


def maxCommon(a, b):
    while b:
        a, b = b, a % b
        print((a, b))
    return a


def minCommon(a, b):
    c = a * b
    while b:
        a, b = b, a % b
        print((a, b))
    return c // a


l = [1, 2, 43, 13, 4, 75, 31, 25]


def median(data):
    data.sort()
    half = len(data) // 2
    return (data[half] + data[~half]) / 2


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


class Singleton1(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton1, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        super(Singleton, cls).__init__(*args, **kwargs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class Single(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Single, cls).__new__(cls, *args, **kwargs)
        return cls._instance


# @singleton
class MyClass(object):
    # def __new__(cls, *args, **kwargs):
    #     print("new")

    __metaclass__ = Singleton

    def __init__(self):
        # print("init")
        self.page = "init"


class Second(MyClass):
    pass


if __name__ == '__main__':
    m = Second()
    m.page = "ll"
    n = Second()
    print(n.page)
    print(m == n)
