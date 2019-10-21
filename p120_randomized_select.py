#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 120页
    随机查找"""

import numpy as np
from a_swap import swap


def partition(lst, start, end):
    middle_value = lst[end]
    middle_index = start - 1
    for index in range(start, end):
        if lst[index] <= middle_value:
            middle_index += 1
            swap(lst, middle_index, index)
    middle_index += 1
    swap(lst, middle_index, end)
    return middle_index


def randomized_partition(lst, start, end):
    middle = np.random.randint(start, end)
    swap(lst, middle, end)
    return partition(lst, start, end)


def randomized_select(lst, ith, start=0, end=-1):
    """get the ith small element of lst[start : end]"""
    if start == end:
        return lst[start]
    if end == -1:
        inner_lst = lst.copy()
        end = len(lst) - 1
    else:
        inner_lst = lst
    middle = randomized_partition(inner_lst, start, end)
    kth = middle - start + 1
    if ith == kth:
        return inner_lst[middle]
    elif ith < kth:
        return randomized_select(inner_lst, ith, start, middle-1)
    else:
        return randomized_select(inner_lst, ith-kth, middle+1, end)


if __name__ == '__main__':
    unsorted = [49, 27, 65, 97, 76, 12, 49, 38]
    # the 3rd small ele is 38
    print(randomized_select(unsorted, 3))