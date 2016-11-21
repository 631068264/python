#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/9/17 17:16
@annotation = '' 
"""

print(套接字.socket)

import select

print(select.select)

from gevent import monkey

monkey.patch_all()

print(套接字.socket)
print(select.select)
