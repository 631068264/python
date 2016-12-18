#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/11/21 19:53
@annotation = '' 
"""
from fabric.api import local, settings, abort
from fabric.context_managers import cd
from fabric.contrib.console import confirm

# fab hello
from fabric.operations import run
from fabric.state import env


def hello():
    print("Hello world!")


# fab hello_name:name=Jeff
# fab hello:Jeff
def hello_name(name="world"):
    print("Hello %s!" % name)


# fab prepare_deploy
def prepare_deploy():
    local("git status")
    local("git add -A && git commit")
    local("git checkout develop")


def test():
    # A setting called warn_only
    # lets you turn aborts into warnings,
    # allowing flexible error handling to occur.
    with settings(warn_only=True):
        result = local('./manage.py test my_app', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")


# run remote
env.hosts = ['wyx@192.168.1.108']


def deploy():
    code_dir = '/srv/django/myproject'
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")
