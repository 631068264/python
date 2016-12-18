#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/11/30 22:46
@annotation = '' 
"""


def echo(value=None):
    print "Execution starts when 'next()' is called for the first time."
    try:
        while True:
            try:
                value = (yield value)
            except Exception, e:
                value = e
    finally:
        print "Don't forget to clean up when 'close()' is called."


if __name__ == '__main__':
    generator = echo(1)
    print generator.next()
    # print generator.next()
    print generator.send(2)
    generator.throw(TypeError, "spam")
    generator.close()
