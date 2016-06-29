#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'

import hello

hello.test()  # 引入模块

# 别名引入 设置引入优先级 增强Python不同版本的一直性
try:
    import cStringIO as StringIO
except ImportError:  # 导入失败会捕获到ImportError
    import StringIO

_xxx, __xx = (7, 8)  # private变量

from pic import Image

im = Image.open('test.png')
print im.format, im.size, im.mode
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')
