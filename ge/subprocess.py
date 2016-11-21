#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/8/22 15:51
@annotation = '' 
"""
import gevent
from gevent.subprocess import Popen, PIPE


def cron():
    while True:
        print("cron")
        gevent.sleep(0.2)


g = gevent.spawn(cron)
sub = Popen(['sleep 1; uname'], stdout=PIPE, shell=True)
out, err = sub.communicate()
g.kill()
print(out.rstrip())
