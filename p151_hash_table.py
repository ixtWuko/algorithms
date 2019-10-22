#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 151页
    散列表-链表法"""

import math


class Hash_table:
    def __init__(self, size):
        self.count = size
        self.items = {}

    def __hash(self, data, method='division'):
        if method == 'multiplication':
            a = (math.sqrt(5) - 1) / 2
            m = math.pow(2, 14)
            return math.floor(math.modf(data * a)[0] * m)
        else:
            return data % self.count

    def hash(self, data, ith=0, method='linear'):
        if method == 'quadratic':
            c1 = 7
            c2 = 8
            return (self.__hash(data) + c1 * ith + c2 * ith * ith) // self.count
        elif method == 'double':
            return (self.__hash(data) + ith * self.__hash(data, method='multiplication')) // self.count
        else:
            return (self.__hash(data) + ith) // self.count

    def insert(self, data):
        ith = 0
        hash_value = self.hash(data, method='double')
        while hash_value in self.items:
            ith += 1
            hash_value = self.hash(data, ith=ith, method='double')
        self.items[hash_value] = data

    def __str__(self):
        return str(self.items)


if __name__ == '__main__':
    data_lst = [49, 27, 65, 97, 76, 12, 38]
    ht = Hash_table(10)
    for ele in data_lst:
        ht.insert(ele)
    print(ht)
