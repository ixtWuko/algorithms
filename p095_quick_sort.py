#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 095页
    快速排序"""

import numpy as np
from a_swap import swap


def quick_sort(lst, start=0, end=-1):
    if end == -1:
        end = len(lst) - 1
    if start < end:
        exchange_index = start - 1
        # randomized middle value
        middle_index = np.random.randint(start, end)
        swap(lst, middle_index, end)
        for i in range(start, end):
            if lst[i] <= lst[end]:
                exchange_index += 1
                swap(lst, i, exchange_index)
        exchange_index += 1
        swap(lst, end, exchange_index)
        if start < exchange_index:
            quick_sort(lst, start, exchange_index-1)
        if exchange_index < end:
            quick_sort(lst, exchange_index+1, end)


if __name__ == '__main__':
    unsorted = [49, 27, 65, 97, 76, 12, 38]
    quick_sort(unsorted)
    print(unsorted)