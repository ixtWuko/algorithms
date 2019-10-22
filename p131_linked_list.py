#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 131页
    链表"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next_ref):
        self.next = next_ref

    def get_prev(self):
        return self.prev

    def set_prev(self, prev_ref):
        self.prev = prev_ref


class Double_linked_list:
    def __init__(self):
        self.head = None

    def __str__(self):
        result = []
        iterator = self.head
        while iterator is not None:
            result.append(iterator.data)
            iterator = iterator.next
        return str(result)

    def insert(self, node):
        node.prev = None
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def insert_data(self, data):
        node = Node(data)
        self.insert(node)

    def delete(self, node):
        # head
        if self.head is node:
            self.head = node.next
            self.head.prev = None
        # tail
        elif node.next is None:
            node.prev.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        del node

    def search(self, data):
        iterator = self.head
        while iterator is not None and iterator.data != data:
            iterator = iterator.next
        return iterator


if __name__ == '__main__':
    n = Node(35)
    print(n, n.next, n.prev)
    unsorted = [49, 27, 65, 97, 76, 12, 38]
    dll = Double_linked_list()
    for ele in unsorted:
        dll.insert_data(ele)
    print(dll)
    n = dll.search(76)
    dll.delete(n)
    print(dll)