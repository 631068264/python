#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'
"""
base64
"""
import base64

print(base64.b64encode('adfsdf7987阿克苏绝地反击'))

print(base64.b64decode('YWRmc2RmNzk4N+mYv+WFi+iLj+e7neWcsOWPjeWHuw=='))

"""
md5
固定的128 bit字节，通常用一个32位的16进制字符串表示
"""
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()

"""
SHA1
160 bit字节，通常用一个40位的16进制字符串表示
"""
import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()

