#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'
"""
 用\d可以匹配一个数字，\w可以匹配一个字母或数字 \s可以匹配一个空格

 特殊字符，在正则表达式中，要用'\'转义

 .可以匹配任意字符，所以
 用*表示任意个字符（包括0个），
 用+表示至少一个字符，
 用?表示0个或1个字符，
 用{n}表示n个字符，用{n,m}表示n-m个字符

 用[]表示范围
 A|B可以匹配A或B，所以[P|p]ython可以匹配'Python'或者'python'

()表示的就是要提取的分组

 ^表示行的开头，^\d表示必须以数字开头。
$表示行的结束，\d$表示必须以数字结束。

.*?

re.S 忽略换行符
re.I 忽略大小写
"""
import re

# test = '12789'
# if re.match(r'\d{5}', test):
#     print 'ok'
# else:
#     print 'failed'
#
# # 切分字符
# list = 'a b   c'.split(' ')
# print(list)
#
# list = re.split(r'\s+', 'a b   c')
# re.split(r'[\s\,\;]+', 'a,b;; c  d')
# print(list)
#
# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# # 注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。
# print(m.groups())
#
# # 贪婪匹配
# lsit = re.match(r'^(\d+?)(0*)$', '102300').groups()
# # ('1023', '00')
# re.match(r'^(\d+)(0*)$', '102300').groups()
# # ('102300', '')




text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

datepat = re.compile(r'\d+/\d+/\d+')
datepat.match(text1)
l = re.search(r'\d+/\d+/\d+', text1)
print l.string

if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print datepat.findall(text)

print text.replace("Today", "Fuck")

print re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

text = 'UPPER PYTHON, lower python, Mixed Python'
print re.findall('python', text, flags=re.IGNORECASE)


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


print re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
