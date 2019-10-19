#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 043页
    矩阵乘法的Strassen算法"""

import numpy as np


def strassen(mat_a, mat_b):
    # origin length
    origin_length = len(mat_a)
    if origin_length == 1:
        return mat_a * mat_b
    # extend length
    extend_length = 1
    while origin_length > extend_length:
        extend_length *= 2
    # diff length
    diff_length = extend_length - origin_length
    if diff_length == 0:
        extend_mat_a = mat_a
        extend_mat_b = mat_b
    else:
        extend_mat_a = np.hstack([
            np.vstack([mat_a, np.zeros([diff_length, origin_length])]),
            np.vstack([np.zeros([origin_length, diff_length]), np.ones([diff_length, diff_length])])
        ])
        extend_mat_b = np.hstack([
            np.vstack([mat_b, np.zeros([diff_length, origin_length])]),
            np.vstack([np.zeros([origin_length, diff_length]), np.ones([diff_length, diff_length])])
        ])
    
    half_length = extend_length // 2
    # slice
    a11 = extend_mat_a[:half_length, :half_length]
    a12 = extend_mat_a[:half_length, half_length:]
    a21 = extend_mat_a[half_length:, :half_length]
    a22 = extend_mat_a[half_length:, half_length:]
    b11 = extend_mat_b[:half_length, :half_length]
    b12 = extend_mat_b[:half_length, half_length:]
    b21 = extend_mat_b[half_length:, :half_length]
    b22 = extend_mat_b[half_length:, half_length:]
    # divide
    p1 = strassen(a11, b12 - b22)
    p2 = strassen(a11 + a12, b22)
    p3 = strassen(a21 + a22, b11)
    p4 = strassen(a22, b21 - b11)
    p5 = strassen(a11 + a22, b11 + b22)
    p6 = strassen(a12 - a22, b21 + b22)
    p7 = strassen(a11 - a21, b11 + b12)
    # merge
    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p5 + p1 - p3 - p7
    mat_c = np.hstack([np.vstack([c11, c21]), np.vstack([c12, c22])])

    if diff_length == 0:
        return mat_c
    else:
        return mat_c[:origin_length, :origin_length]

    # first version
    # suppose that the size of matrix is always 2^n
    # if len(mat_a) == 1:
    #     return mat_a * mat_b
    # half_length = len(mat_a) // 2
    # # slice
    # a11 = mat_a[:half_length, :half_length]
    # a12 = mat_a[:half_length, half_length:]
    # a21 = mat_a[half_length:, :half_length]
    # a22 = mat_a[half_length:, half_length:]
    # b11 = mat_b[:half_length, :half_length]
    # b12 = mat_b[:half_length, half_length:]
    # b21 = mat_b[half_length:, :half_length]
    # b22 = mat_b[half_length:, half_length:]
    # # divide
    # p1 = strassen(a11, b12 - b22)
    # p2 = strassen(a11 + a12, b22)
    # p3 = strassen(a21 + a22, b11)
    # p4 = strassen(a22, b21 - b11)
    # p5 = strassen(a11 + a22, b11 + b22)
    # p6 = strassen(a12 - a22, b21 + b22)
    # p7 = strassen(a11 - a21, b11 + b12)
    # # merge
    # c11 = p5 + p4 - p2 + p6
    # c12 = p1 + p2
    # c21 = p3 + p4
    # c22 = p5 + p1 - p3 - p7
    # mat_c = np.hstack([np.vstack([c11, c21]), np.vstack([c12, c22])])
    # return mat_c


if __name__ == '__main__':
    matrix_size = np.random.randint(1, 100)
    matrix_a = np.random.random([matrix_size, matrix_size])
    matrix_b = np.random.random([matrix_size, matrix_size])
    print(np.matmul(matrix_a, matrix_b))
    print(strassen(matrix_a, matrix_b))
    print(matrix_size)

