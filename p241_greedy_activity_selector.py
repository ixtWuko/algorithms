#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 241页
    贪心算法 活动选择"""


def greedy_activity_selector(s, f):
    """
    参见《算法导论》第16章
    :param s: 所有活动的开始时间
    :param f: 所有活动的结束时间
    :return: 活动序列
    """
    n = len(s)
    result = [1]
    k = 1
    for m in range(1, n):
        if s[m] >= f[k]:
            result.append(m+1)
            k = m
    return result


if __name__ == '__main__':
    start_time = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    finish_time = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    print(greedy_activity_selector(start_time, finish_time))