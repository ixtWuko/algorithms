#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 070页
    随机排列数组"""

import numpy as np
from a_swap import *


def permute_by_sorting(lst):
    length = len(lst)
    p = np.random.random(length)
    # p = lst.copy()
    # sort lst using p as key
    for i in range(0, length):
        for j in range(1, length-i):
            if p[j-1] > p[j]:
                swap(p, j-1, j)
                swap(lst, j-1, j)


if __name__ == '__main__':
    unsorted = [49, 27, 65, 97, 76, 12, 38]
    permute_by_sorting(unsorted)
    print(unsorted)