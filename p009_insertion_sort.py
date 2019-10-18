#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 009页
    插入排序 """


def insertion_sort(lst):
    length = len(lst)
    rhs = 1
    while rhs < length:
        # method 1
        value_tmp = lst[rhs]
        lhs = rhs - 1
        while lhs >= 0 and lst[lhs] > value_tmp:
            lst[lhs + 1] = lst[lhs]
            lhs -= 1
        lst[lhs + 1] = value_tmp
        rhs += 1

        # method 2
        # lhs = 0
        # while lhs < rhs and lst[lhs] < lst[rhs]:
        #     lhs += 1
        # if lhs < rhs:
        #     value_tmp = lst[rhs]
        #     rhs_tmp = rhs
        #     while rhs_tmp >= lhs:
        #         lst[rhs_tmp] = lst[rhs_tmp - 1]
        #         rhs_tmp -= 1
        #     lst[lhs] = value_tmp
        # rhs += 1


if __name__ == '__main__':
    unsorted = [49, 27, 65, 97, 76, 12, 38]
    insertion_sort(unsorted)
    print(unsorted)
