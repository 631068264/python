#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/10/27 16:19
@annotation = '' 
"""
import Queue
import socket

# create a socket
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
# set option reused
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('', 10001)
server.bind(server_address)

server.listen(10)

# sockets from which we except to read
inputs = [server]

# sockets from which we expect to write
outputs = []

# Outgoing message queues (socket:Queue)
message_queues = {}

# A optional parameter for select is TIMEOUT
timeout = 20
"""
减少上下文(程序执行状态)切换开销 就绪 运行 阻塞   新建 终止
select 最大连接数限制 采用轮询
poll   与select 没有最大连接数限制 采用轮询
epoll   采用类似回调的机制

就绪通知技
就绪通知维护一个状态，由用户读取。 (轮询)
异步IO由系统调用用户的回调函数。就绪通知在数据就绪时就生效，而异步IO直到数据IO完成才发生回调 (callback)

使用非阻塞函数，就不存在阻塞IO导致上下文切换


"""
while inputs:
    print "waiting for next event"
    readable, writable, exceptional = select.select(inputs, outputs, inputs, timeout)

    # When timeout reached , select return three empty lists
    if not (readable or writable or exceptional):
        print "Time out ! "
        break

    for s in readable:
        if s is server:
            # A "readable" socket is ready to accept a connection
            connection, client_address = s.accept()
            print "    connection from ", client_address
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = Queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                print " received ", data, "from ", s.getpeername()
                message_queues[s].put(data)
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)
            else:
                # Interpret empty result as closed connection
                print "  closing", client_address
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                # remove message queue
                del message_queues[s]
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except Queue.Empty:
            print " ", s.getpeername(), 'queue empty'
            outputs.remove(s)
        else:
            print " sending ", next_msg, " to ", s.getpeername()
            s.send(next_msg)

    for s in exceptional:
        print " exception condition on ", s.getpeername()
        # stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        # Remove message queue
        del message_queues[s]
