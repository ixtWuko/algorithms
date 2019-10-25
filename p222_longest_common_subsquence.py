#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 222页
    最长公共子序列"""

import numpy as np


def longest_common_subsquence(x, y):
    m = len(x)
    n = len(y)
    if m == 0 or n == 0:
        return ''
    c = np.zeros([m+1, n+1])
    b = np.zeros([m+1, n+1])
    # 2 for left, 3 for left-up, 4 for up
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 3
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 4
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 2
    result = ''
    while m > 0 and n > 0:
        if b[m][n] == 3:
            result = x[m-1] + result
            m, n = m-1, n-1
        elif b[m][n] == 4:
            m -= 1
        elif b[m][n] == 2:
            n -= 1
        else:
            break
    return result


if __name__ == '__main__':
    str_x = 'ABCBDAB'
    str_y = 'BDCABA'
    print(longest_common_subsquence(str_x, str_y))

