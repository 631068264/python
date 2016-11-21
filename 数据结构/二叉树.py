#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/10/26 20:23
@annotation = '' 
"""
from collections import deque


class Node(object):
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def search(self, data):
        current = self.root
        while current.data != data:
            if data < current.data:
                current = current.left
            else:
                current = current.right
            if current is None:
                return None
        print current.data
        return current

    def insert(self, data):
        temp = Node()
        temp.data = data
        if self.root is None:
            self.root = temp
        else:
            current = self.root
            while True:
                previous = current
                if data < current.data:
                    current = current.left
                    if current is None:
                        previous.left = temp
                        return
                else:
                    current = current.right
                    if current is None:
                        previous.right = temp
                        return

    def preOrder(self, root):
        if root is not None:
            print root.data,
            self.preOrder(root.left)
            self.preOrder(root.right)

    def pre_Order(self, root):
        stack = []
        current = root
        while current is not None or len(stack) != 0:
            if current:
                print current.data,
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right

    def inOrder(self, root):
        if root is not None:
            self.inOrder(root.left)
            print root.data,
            self.inOrder(root.right)

    def in_Order(self, root):
        stack = []
        current = root
        while current is not None or len(stack) != 0:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                print current.data,
                current = current.right

    def postOrder(self, root):
        if root is not None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print root.data,

    def post_Order(self, root):
        stack = []
        current = root
        previous = None
        while current is not None or len(stack) != 0:
            while current is not None:
                stack.append(current)
                current = current.left
            if stack[-1].right is not previous:
                current = stack[-1].right
                previous = None
            else:
                previous = stack.pop()
                print previous.data,

    def levelOrder(self, root):
        if not root:
            return
        q = deque([root])
        while q:
            current = q.popleft()
            print current.data,
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)


if __name__ == '__main__':
    tree = Tree()
    tree.insert(50)
    tree.insert(25)
    tree.insert(75)
    tree.insert(12)
    tree.insert(37)
    tree.insert(43)
    tree.insert(30)
    tree.insert(33)
    tree.insert(87)
    tree.insert(86)
    tree.insert(97)

    # tree.levelOrder(tree.root)

    tree.preOrder(tree.root)
    print
    tree.pre_Order(tree.root)

    print
    tree.inOrder(tree.root)
    print
    tree.in_Order(tree.root)

    print
    tree.postOrder(tree.root)
    print
    tree.post_Order(tree.root)
    print

    tree.search(12)
