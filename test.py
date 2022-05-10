

import math


def fn1(n, i):
    res = 0
    curr = math.ceil((n - i) / 2)
    for i in range(i + 1):
        res += 1/curr
        curr += 1
    return res

def fn2(n, i):
    res = 0
    curr = math.ceil((n - 3 * i) / 2)
    for i in range((n - i) // 2 + 1):
        res += 1 / curr
        curr += 1
    return res

def fn3(n, i):
    res = 0
    curr = math.ceil((n - i) / 2)
    for i in range((n - 3 * i) // 2 + 1):
        res += 1 / curr
        curr += 1
    return res

for i in range(10, 10000):
    print(i, fn1(i, 1) + fn2(i, 1) + fn3(i, 1))