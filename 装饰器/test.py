#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/10/18 21:31
@annotation = '' 
"""


def log(func):
    def wrapper(*args, **kwargs):
        print "Call before %s" % func.__name__
        result = func(*args, **kwargs)
        print "Call after"
        return result

    return wrapper


def strong_log(desc):
    def new_deco(old_handler):
        def new_handler(*args, **kwargs):
            print "Call before"
            result = old_handler(*args, **kwargs)
            print "Call %s" % desc
            return result

        return new_handler

    return new_deco

@log
def test():
    print "Try"
    return "Hello"


if __name__ == '__main__':
    print test()
