#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 129页
    栈与队列"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, ele):
        self.items.append(ele)

    def pop(self):
        return self.items.pop()


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, ele):
        self.items.append(ele)

    def dequeue(self):
        return self.items.pop(0)