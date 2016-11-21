#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/10/26 22:54
@annotation = '' 
"""


class Node(object):
    def __init__(self):
        self.data = None
        self.n = None


class Link(object):
    def __init__(self):
        self.head = None

    def add_front(self, data):
        temp = Node()
        temp.data = data
        temp.n = self.head
        self.head = temp

    def add_after(self, data):
        temp = Node()
        temp.data = data

        if self.head is None:
            self.head = temp
        else:
            current = self.head
            while current.n:
                current = current.n
            current.n = temp

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.n
            return
        temp = self.head
        while temp:
            previous = temp
            temp = temp.n
            if temp.data == data:
                previous.n = temp.n
                break

    def print_link(self):
        temp = self.head
        while temp:
            print temp.data,
            temp = temp.n

    def reverse(self):
        if self.head:
            tail = None
            current = self.head
            while current:
                future = current.n
                current.n = tail
                tail = current
                current = future
            self.head = tail
            self.print_link()


if __name__ == '__main__':
    link = Link()
    link.add_after(1)
    link.add_after(2)
    link.add_after(3)
    link.add_after(4)

    link.print_link()
    print
    link.reverse()

    print
    link.delete(4)
    link.print_link()
