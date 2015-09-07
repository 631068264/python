#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'
"""
只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。
现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。

请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，
否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，
因为__init__.py本身就是一个模块，而它的模块名就是mycompany。


任何模块代码的第一个字符串都被视为模块的文档注释；

import 包名.模块名
"""

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print 'Hello, world!'
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'


if __name__ == '__main__':
    test()

_xxx, __xx = (7, 8)  # private变量


# private 函数
def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

# 这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。


# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
#
# 运行python hello.py获得的sys.argv就是['hello.py']；
#
# 运行python hello.py Michael获得的sys.argv就是['hello.py', 'Michael]。
