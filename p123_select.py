#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 123页
    选择算法"""

from a_swap import swap
from p095_quick_sort import quick_sort


def median(lst):
    """return the small median of list"""
    tmp_lst = lst.copy()
    quick_sort(tmp_lst)
    return tmp_lst[(len(lst)-1) // 2]


def partition(lst, median_value):
    """divide lst by median_value and return the index of median_value"""
    middle_index = -1
    for i in range(len(lst)):
        if lst[i] <= median_value:
            middle_index += 1
            swap(lst, middle_index, i)
            if lst[middle_index] == median_value:
                self_index = middle_index
    swap(lst, middle_index, self_index)
    return middle_index


def select(lst, ith):
    if lst == [] or ith > len(lst):
        return None
    group_size = 5
    group_count = len(lst) // group_size
    if len(lst) % group_size != 0:
        group_count += 1
    if group_count == 1:
        tmp_lst = lst.copy()
        quick_sort(tmp_lst)
        return tmp_lst[ith-1]

    median_values = []
    for i in range(group_count-1):
        median_values.append(median(lst[i * group_size: i * group_size + group_size]))
    median_values.append(median(lst[(group_count-1) * group_size:]))
    median_value = select(median_values, (group_count - 1) // 2)
    kth = partition(lst, median_value) + 1
    if kth == ith:
        return median_value
    elif kth > ith:
        return select(lst[:kth-1], ith)
    else:
        return select(lst[kth:], ith-kth)


if __name__ == '__main__':
    unsorted = [49, 27, 65, 97, 76, 12, 49, 38, 9, 99, 47, 32, 132, 65, 34, 78, 47, 32, 16, 87, 0]
    for index in range(len(unsorted)):
        print(select(unsorted, index+1))