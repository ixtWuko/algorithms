#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 043页
    矩阵乘法的Strassen算法"""

import numpy as np


def strassen(mat_a, mat_b):
    if len(mat_a) == 1:
        return mat_a * mat_b
    half_length = len(mat_a) // 2
    # slice
    a11 = mat_a[:half_length, :half_length]
    a12 = mat_a[:half_length, half_length:]
    a21 = mat_a[half_length:, :half_length]
    a22 = mat_a[half_length:, half_length:]
    b11 = mat_b[:half_length, :half_length]
    b12 = mat_b[:half_length, half_length:]
    b21 = mat_b[half_length:, :half_length]
    b22 = mat_b[half_length:, half_length:]
    # divide
    p1 = strassen(a11, b12-b22)
    p2 = strassen(a11+a12, b22)
    p3 = strassen(a21+a22, b11)
    p4 = strassen(a22, b21-b11)
    p5 = strassen(a11+a22, b11+b22)
    p6 = strassen(a12-a22, b21+b22)
    p7 = strassen(a11-a21, b11+b12)
    # merge
    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p5 + p1 - p3 - p7
    mat_c = np.hstack([np.vstack([c11, c21]), np.vstack([c12, c22])])
    return mat_c


if __name__ == '__main__':
    matrix_a = np.random.random([8, 8])
    matrix_b = np.random.random([8, 8])
    print(np.matmul(matrix_a, matrix_b))
    print(strassen(matrix_a, matrix_b))