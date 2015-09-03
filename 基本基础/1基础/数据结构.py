#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'


"""
list是一种有序的集合，可以随时添加和删除其中的元素。
append（object） 尾插
insert(index,object) 定位插
pop() 返回尾 删除
pop(index) 删除

array.sort()

len(object)
str.replace(tar,src)
"""
classmate1 = ['Michael', 'Bob', 'Tracy']
print(classmate1)
print(len(classmate1))
print(classmate1[1])

classmates = [2, 'Bob', '45']
print(classmates)
print(len(classmates))
print(classmates[0])

classmates.append(classmate1)
print(classmates)
print(len(classmates))  # 4


"""
tuple一旦初始化就不能修改
tuple 和 list 可以结合在一起
"""
classmates = ('Michael', 'Bob', 'Tracy')

"""
dict ==> Map
pop(key)
"""
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
print('Thomas' in d)  # 判断存在
print(d.get('Michael'))
print(d.get('Thomas', -1))

"""
set
add(key)
remove(key) & | 交并集
"""
s = set([1, 1, 2, 2, 3, 3])
print(s)