#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'
try:
    import cPickle as pickle
except ImportError:
    import pickle
# 序列化
d = dict(name='Bob', age=20, score=88)
str = pickle.dumps(d)

# 反序列化
"""
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)
"""

import json

"""
JSON类型	Python类型
{}	        dict
[]	        list
"string"	'str'或u'unicode'
1234.56	    int或float
true/false	True/False
null	None
"""
d = dict(name='Bob', age=20, score=88)
j = json.dumps(d)
print(j)
s = json.loads(j)
print(s)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


s = Student('Bob', 789, 123)
print(s.age)
c = json.dumps(s, default=lambda obj: obj.__dict__)
print(c)

b = json.loads(c, object_hook=dict2student)
print(b.name)
