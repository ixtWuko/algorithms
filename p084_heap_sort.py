#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 084页
    堆排序"""

from a_swap import *

def parent(index):
    return (index - 1) // 2


def left(index):
    return index * 2 + 1


def right(index):
    return index * 2 + 2


class Heap:
    data = []

    def __max_heapify(self, index, lst=None):
        """suppose left(i) and right(i) is already a heap"""
        if lst is None:
            lst = self.data
        lhs = left(index)
        rhs = right(index)
        if lhs < len(lst) and lst[lhs] > lst[index]:
            largest = lhs
        else:
            largest = index
        if rhs < len(lst) and lst[rhs] > lst[largest]:
            largest = rhs
        if largest != index:
            swap(lst, largest, index)
            self.__max_heapify(largest)

    def __init__(self, lst):
        self.data = lst.copy()
        for i in range(len(lst) // 2, -1, -1):
            self.__max_heapify(i)

    def heap_sort(self):
        unsorted_lst = self.data.copy()
        sorted_lst = []
        while len(unsorted_lst) > 0:
            sorted_lst.append(unsorted_lst.pop(0))
            self.__max_heapify(0, unsorted_lst)
        sorted_lst.reverse()
        return sorted_lst

    def max(self):
        if len(self.data) > 0:
            return self.data[0]
        return None

    def extract_max(self):
        if len(self.data) > 0:
            max_value = self.data[0]
            self.data[0] = self.data[-1]
            self.data.pop()
            self.__max_heapify(0)
            return max_value
        return None

    def increase_key(self, index, key):
        self.data[index] = key
        p = parent(index)
        while index > 0 and self.data[p] < self.data[index]:
            value_tmp = self.data[p]
            self.data[p] = self.data[index]
            self.data[index] = value_tmp
            index = p
            p = parent(index)

    def insert(self, value):
        self.data.append(value)
        self.increase_key(len(self.data)-1, value)


if __name__ == '__main__':
    unsorted = Heap([49, 27, 65, 97, 76, 12, 38])

    print(unsorted.data)
    print(unsorted.heap_sort())

    print(unsorted.extract_max())
    print(unsorted.data)
    print(unsorted.heap_sort())

    unsorted.insert(36)
    print(unsorted.data)
    print(unsorted.heap_sort())

    unsorted.insert(103)
    print(unsorted.data)
    print(unsorted.heap_sort())