#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 023页
    冒泡排序"""


def bubble_sort(lst):
    for i in range(1, len(lst)):
        for j in range(len(lst) - i):
            if lst[j] > lst[j+1]:
                value_tmp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = value_tmp


if __name__ == '__main__':
    unsorted = [49, 27, 65, 97, 76, 12, 38]
    bubble_sort(unsorted)
    print(unsorted)