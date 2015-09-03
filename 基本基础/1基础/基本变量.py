#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'

# \\代表字符 \
# 字符串换行 \n
# 一个布尔值只有True、False两种值  布尔值可以用and、or和not运算。
# 空值None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
print(3 > 2)
"""
a = 'ABC'
时，Python解释器干了两件事情：

在内存中创建了一个'ABC'的字符串；

在内存中创建了一个名为a的变量，并把它指向'ABC'
"""
a = 'ABC'
b = a
a = 'XYZ'
print b

print 10 / 3
print 10.0 / 3

# 字符
print ord('A')
print chr(65)
print('疯狂手机费啦')
# 返回字符串长度
print len('abc')

# 格式化输出
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
"""
%d	整数
%f	浮点数
%s	字符串 把任何类型转成字符串
%x	十六进制整数
用%%来表示一个%
"""
# int() 类型转换  raw_input()读取的内容永远以字符串的形式返回

isinstance(x, str)
isinstance(x, (int, float))
