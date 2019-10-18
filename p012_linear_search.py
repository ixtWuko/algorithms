#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 012页
    线性查找"""


def linear_search(lst, value):
    index_lst = []
    for i in range(len(lst)):
        if lst[i] == value:
            index_lst.append(i)
    return index_lst


if __name__ == '__main__':
    lst = [49, 27, 65, 97, 76, 12, 49, 38]
    print(linear_search(lst, 49))