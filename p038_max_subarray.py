#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 038页
    最大子数组
    从左侧最大子数组、右侧最大子数组、跨中间最大子数组中选最大的 """


def max_subarray(lst, start=0, end=-1):
    if end == -1:
        end = len(lst) - 1
    if start == end:
        return {'start_index': start, 'end_index': end, 'sum': lst[start]}
    middle = (end - start) // 2 + start

    # crossing
    total_sum = lst[middle]
    lhs_sum = total_sum
    lhs = middle
    for i in range(middle - 1, start - 1, -1):
        total_sum += lst[i]
        if total_sum > lhs_sum:
            lhs_sum = total_sum
            lhs = i
    total_sum = lst[middle + 1]
    rhs_sum = total_sum
    rhs = middle + 1
    for i in range(middle + 2, end):
        total_sum += lst[i]
        if total_sum > rhs_sum:
            rhs_sum = total_sum
            rhs = i
    crossing_max_subarray = {'start_index': lhs, 'end_index': rhs, 'sum': lhs_sum + rhs_sum}

    # left and right
    left_max_subarray = max_subarray(lst, start, middle)
    right_max_subarray = max_subarray(lst, middle + 1, end)

    # compare
    if crossing_max_subarray['sum'] > left_max_subarray['sum'] and \
            crossing_max_subarray['sum'] > right_max_subarray['sum']:
        return crossing_max_subarray
    elif left_max_subarray['sum'] > right_max_subarray['sum']:
        return left_max_subarray
    else:
        return right_max_subarray


if __name__ == '__main__':
    unsorted = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, 4, 7]
    print(max_subarray(unsorted))