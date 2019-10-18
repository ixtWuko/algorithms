#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 022页
    二分查找"""

from p017_merge_sort import *


def binary_search(lst, value):
    index_lst = []
    start = 0
    end = len(lst) - 1
    while start < end:
        index = (end - start) // 2 + start
        if lst[index] < value:
            start = index + 1
        elif lst[index] > value:
            end = index - 1
        else:  # lst[index] == value
            while lst[index] == value:
                index -= 1
            index += 1
            while lst[index] == value:
                index_lst.append(index)
                index += 1
            break
    return index_lst


if __name__ == '__main__':
    search_lst = [49, 27, 65, 97, 76, 12, 49, 38]
    merge_sort(search_lst)
    print(search_lst)
    print(binary_search(search_lst, 49))
