#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''a module to calculate the gcd of two number using Euclid algorithm
result = gcd(a,b) '''

# 欧几里得算法求最大公约数

def gcd(a, b):
    s = max(a,b)
    r = min(a,b)
    while r != 0:
        temp = r
        r = s % r
        s = temp
    return s

if __name__ == '__main__':
    print(gcd(225, 252))