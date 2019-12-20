#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 017页
    归并排序
    排序的过程主要在于归并过程 """


def merge(lst, start, middle, end):
    lhs = start
    rhs = middle + 1
    sorted_lst = []
    while lhs <= middle and rhs <= end:
        if lst[lhs] < lst[rhs]:
            sorted_lst.append(lst[lhs])
            lhs += 1
        else:
            sorted_lst.append(lst[rhs])
            rhs += 1
    while lhs <= middle:
        sorted_lst.append(lst[lhs])
        lhs += 1
    while rhs <= end:
        sorted_lst.append(lst[rhs])
        rhs += 1
    for i in range(len(sorted_lst)):
        lst[start + i] = sorted_lst[i]


def merge_sort(lst, start=0, end=-1):
    if end == -1:
        end = len(lst) - 1
    if end > start:
        middle = (end - start) // 2 + start
        if middle > start:
            merge_sort(lst, start, middle)
        if end > middle + 1:
            merge_sort(lst, middle+1, end)
        merge(lst, start, middle, end)


if __name__ == '__main__':
    unsorted = [49, 27, 65, 97, 76, 12, 38]
    merge_sort(unsorted)
    print(unsorted)
