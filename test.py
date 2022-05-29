

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

def fn4(n, i):
    res = 0
    curr = math.ceil((n - 2*i) / 4)
    for i in range(n // 2 + 1):
        res += 1 / curr
        curr += 1
    return res

def fn5(n, i):
    res = 0
    curr = math.ceil((n - 2*i) / 4)
    for i in range(math.ceil((n - 2*i) / 2)):
        res += 1 / curr
        curr += 1
    return res

x = 1
for i in range(500*x, 1000000*x, 500*x):
    print(i, fn4(i, x) + 2 * fn5(i, x))
