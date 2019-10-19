#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 024页
    逆序对"""


def inversions(lst):
    pair_lst = []
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i] > lst[j]:
                pair_lst.append([i, j])
    return pair_lst


if __name__ == '__main__':
    unsorted = [49, 27, 65, 97, 76, 12, 38]
    print(inversions(unsorted))