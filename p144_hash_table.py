#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 144页
    散列表-链表法"""

import math


class Hash_table:
    def __init__(self, size):
        self.count = size
        self.items = [None for i in range(size)]

    def hash(self, data, method='division'):
        if method == 'multiplication':
            a = (math.sqrt(5) - 1) / 2
            m = math.pow(2, 14)
            return math.floor(math.modf(data * a)[0] * m)
        else:
            return data % self.count

    def insert(self, data):
        hash_value = self.hash(data)
        if self.items[hash_value] is None:
            self.items[hash_value] = [data]
        else:
            self.items[hash_value].append(data)

    def __str__(self):
        result = {}
        for i in range(self.count):
            result[i] = self.items[i]
        return str(result)


if __name__ == '__main__':
    data_lst = [49, 27, 65, 97, 76, 12, 38]
    ht = Hash_table(10)
    for ele in data_lst:
        ht.insert(ele)
    print(ht)
