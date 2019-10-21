#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 108页
    计数排序"""


def counting_sort(lst):
    # using dict to save memory
    counter = {}
    for i in range(len(lst)):
        if lst[i] in counter:
            counter[lst[i]] += 1
        else:
            counter[lst[i]] = 1
    index = 0
    # it can be changed to a one-iteration way,
    # but this way has the same time complexity
    # because the purpose is copying all value back to lst
    # and its time complexity is always len(lst)
    while len(counter) > 0:
        min_value = min(counter.keys())
        for i in range(counter[min_value]):
            lst[index+i] = min_value
        index += counter[min_value]
        counter.pop(min_value)


if __name__ == '__main__':
    unsorted = [49, 27, 65, 97, 76, 12, 38]
    counting_sort(unsorted)
    print(unsorted)