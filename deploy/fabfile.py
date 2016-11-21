#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/11/21 19:53
@annotation = '' 
"""


# fab hello
def hello():
    print("Hello world!")


# fab hello_name:name=Jeff
# fab hello:Jeff
def hello_name(name="world"):
    print("Hello %s!" % name)


from fabric.api import local


# fab prepare_deploy
def prepare_deploy():
    local("git add -A && git commit")
    local("git push")
