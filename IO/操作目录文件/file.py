#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'
import os

print(os.path.abspath(''))  # 查看当前目录的绝对路径
path = os.path.abspath('')

# 正确处理不同操作系统的路径分隔符
dirPath = os.path.join(path, 'dir')  # 路径合并 不用加/
print(dirPath)

os.makedirs('a/b/c')
os.mkdir(dirPath)  # 然后创建一个目录
os.rmdir(dirPath)  # 删掉一个目录:

# 一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('/Users/michael/testdir/file.txt'))
# 文件扩展名
print(os.path.splitext('/Users/michael/testdir/file.txt'))
"""
# 对文件重命名:
os.rename('xxx.txt', 'test.py')
# 删掉文件:
os.remove('test.py')
"""
# 列出当前目录下的所有目录
[x for x in os.listdir('.') if os.path.isdir(x)]
# 列出所有的.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
