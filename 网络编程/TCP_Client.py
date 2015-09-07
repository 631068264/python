#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'
# 导入socket库:
"""
AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6
SOCK_STREAM指定使用面向流的TCP协议
"""
import socket

"""
# Client
# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))

# 发送数据:
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)

# 关闭连接:
s.close()

header, html = data.split('\r\n\r\n', 1) #分割1次
print header
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print s.recv(1024)
for data in ['Michael', 'Tracy', 'Sarah']:
    # 发送数据:
    s.send(data)
    print s.recv(1024)
s.send('exit')
s.close()
