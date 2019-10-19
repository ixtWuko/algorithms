#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 080页
    随机查找"""

import numpy as np


def random_search(lst, value):
    length = len(lst)
    random_index = np.random.randint(0, length)
    while lst[random_index] != value:
        random_index = np.random.randint(0, length)
    return random_index


if __name__ == '__main__':
    unsorted = [49, 27, 65, 97, 76, 12, 38]
    print(random_search(unsorted, 65))