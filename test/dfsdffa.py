#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'

count = 0
total = 24
key = ""
dic = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
}
while count < total:

    if count % 4 == 0:
        print "A"
        key = "A"
    elif count % 4 == 1:
        print "B"
        key = "B"
    elif count % 4 == 2:
        print "C"
        key = "C"
    elif count % 4 == 3:
        print "D"
        key = "D"

    x = raw_input()
    if x == "q":
        break
    dic[key].append(x)
    count += 1

print dic