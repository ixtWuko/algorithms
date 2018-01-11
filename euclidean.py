# 欧几里得算法求最大公约数

def gcd(a, b):
    s = max(a,b)
    r = min(a,b)
    while r != 0:
        temp = r
        r = s % r
        s = temp
    return s

print(gcd(225, 252))