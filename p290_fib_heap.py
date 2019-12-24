#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 290页
    斐波那契堆
    """


class Fib_heap_node(object):
    def __init__(self, key=None):
        self.key = key
        self.parent = None
        self.right = self
        self.left = self
        self.child = None
        self.degree = 0
        self.mark = None
    def size(self):
        size_sum = 1
        if self.child:
            current_child = self.child
            for i in range(self.degree):
                size_sum += current_child.size()
                current_child = current_child.right
        return size_sum


class Fib_heap(object):
    def __init__(self):
        self.min = None
        self.n = 0
    def insert_node(self, node):
        node.mark = False
        if self.min:
            left_node = self.min.left
            right_node = self.min
            left_node.right = node
            node.left = left_node
            right_node.left = node
            node.right = right_node
            self.n += node.size()
            if node.key < self.min.key:
                self.min = node
        else:
            self.min = node
            self.n = node.size()
    def insert(self, key):
        node = Fib_heap_node(key)
        self.insert_node(node)
    
    def min_node(self):
        return self.min
    def min(self):
        return self.min.key

    def union(self, h):
        if self.min and h.min:
            left_node = self.min.left
            right_node = self.min
            h_left_node = h.min.left
            h_right_node = h.min

            left_node.right = h_right_node
            h_right_node.left = left_node
            right_node.left = h_left_node
            h_left_node.right = right_node
            self.n += h.n
            if h.min.key < self.min.key:
                self.min = h.min
        elif h.min:
            self.min = h.min
            self.n = h.n
    
    def link(self, x, y):
        if x.key < y.key:
            x, y = y, x
        y.left.right = y.right
        y.right.left = y.left
        if x.child:
            left_node = x.child.left
            right_node = x.child
            left_node.right = y
            y.left = left_node
            right_node.left = y
            y.right = right_node
        else:
            x.child = y
        x.degree += 1
        y.mark = False
        return x
    def consolidate(self):
        start_node = self.min
        current_node = start_node.right
        degree = 1
        while current_node is not start_node:
            degree += 1
            current_node = current_node.right

        degree_array = {}
        for i in range(degree):
            next_node = current_node.right
            while current_node.degree in degree_array:
                another_node = degree_array[current_node.degree]
                degree_array.pop(another_node.degree)
                current_node = self.link(current_node, another_node)
            degree_array[current_node.degree] = current_node
            current_node = next_node
        self.min = None
        for ele in degree_array.items:
            if self.min:
                if ele.key < self.min.key:
                    self.min = ele
            else:
                self.min = ele
    def extract_min(self):
        z = self.min
        root_linklist = z.left.left
        if z:
            child = z.child
            for i in range(z.degree):
                left_node = root_linklist
                right.node = root_linklist.right
                left_node.right = child
                child.left = left_node
                right_node.left = child
                child.right = right_node
                child.parent = None
                child = child.right
            left_node = z.left
            right_node = z.right
            left_node.right = right_node
            right_node.left = left_node
            if z if z.right:
                self.min = None
            else:
                self.min = z.right
                consolidate()
            self.n -= 1
        return z
            

    def cut(self, x, y):
        ''' x is a child of y '''
        left_node = x.left
        right_node = x.right
        left_node.right = right_node
        right_node.left = left_node
        y.degree -= 1

        left_node = self.min.left
        right_node = self.min
        left_node.right = x
        x.left = left_node
        right_node.left = x
        x.right = right_node
        x.parent = None
        x.mark = False
    def cascading_cut(self, y):
        z = y.parent
        if z is not None:
            if y.mark == False:
                y.mark = True
            else:
                self.cut(y, z)
                self.cascading_cut(z)
    def decrease_key(self, node, key):
        if key > node.key:
            print("new key is greater than current key")
        node.key = key
        y = node.parent
        if y and node.key < y.key:
            self.cut(node, y)
            self.cascading_cut(y)
        if node.key < self.min.key:
            self.min = node

    def delete(self, node):
        self.decrease_key(node, float('-sinf')):
        self.extract_min()