#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 207页
    动态规划-切钢条"""


def bottom_up_cut_rod(length):
    incomes = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    methods = [[], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
    for l in range(2, length+1):
        income_l = 0
        method_l = []
        for i in range(1, l // 2 + 1):
            if incomes[i] + incomes[l-i] > income_l:
                income_l = incomes[i] + incomes[l-i]
                method_l = methods[i] + methods[l-i]
        if l < len(incomes):
            if income_l <= incomes[l]:
                continue
            incomes[l] = income_l
            methods[l] = method_l
        else:
            incomes.append(income_l)
            methods.append(method_l)
    return [incomes, methods]

def memoized_cut_rod(length):
    incomes = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    max_income = 0
    if length < len(incomes):
        max_income = max(max_income, incomes[length])
    for i in range(1, length // 2 + 1):
        max_income = max(max_income, memoized_cut_rod(i) + memoized_cut_rod(length-i))
    return max_income


if __name__ == '__main__':
    inc, met = bottom_up_cut_rod(40)
    for ele in range(len(inc)):
        print('length = ', ele)
        print('max income = ', inc[ele])
        print('cut method = ', met[ele])
        # print('memoized method = ', memoized_cut_rod(ele))
        print('-' * 30)




