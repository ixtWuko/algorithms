#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 129页, 259页
    栈与队列"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, ele):
        self.items.append(ele)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def multipop(self, k):
        result = []
        while k > 0:
            result.append(self.pop())
            k -= 1
        return result



class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, ele):
        self.items.append(ele)

    def dequeue(self):
        return self.items.pop(0)