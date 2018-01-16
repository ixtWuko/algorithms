#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''a module to calculate the n-th number of fibonacci and fibonacci list less than a input'''

def fibonacci_nth(n):
    result = []
    for i in range(n+1)[1:]:
        if i == 1 or i == 2:
            result.append(1)
        else:
            temp = result[-1] + result[-2]
            result.append(temp)
            result.pop(0)
    return result[-1]

def fibonacci(n):
    result = []
    for i in range(n+1)[1:]:
        if i == 1 or i == 2:
            result.append(1)
        else:
            temp = result[-1] + result[-2]
            result.append(temp)
    return result

if __name__ == '__main__':
    print(fibonacci_nth(25))
    print(fibonacci(25))