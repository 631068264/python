#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'

# 'rb' 读二进制文件
"""
f = open('xx.txt', 'r')
print(f.read())
f.close()
"""

# with 用法
"""
try:
    f = open('/path/to/file', 'r')
    print f.read()
finally:
    if f:
        f.close()
"""
"""相当于 try finally
with open('xx.txt', 'r') as f:
    print f.read()
"""

# 调用read()会一次性读取文件的全部内容，内存就爆了，
# 反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list

# 如果文件很小，read()一次性读取最方便；
# 如果不能确定文件大小，反复调用read(size)比较保险；
# 如果是配置文件，调用readlines()最方便：
with open('xx.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())  # 把末尾的'\n'删掉

with open('xx.txt', 'r') as f:
    while True:
        str = f.read()
        if not str:
            break
        print(str)
