# 生成斐波那契数列
# 大量的数据可能导致溢出

def fibonacci_nth(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_nth(n-1) + fibonacci_nth(n-2)
    return 0


def fibonacci(n):
    result = []
    for i in range(n+1)[1:]:
        result.append(fibonacci_nth(i))
    return result

print(fibonacci(25))
