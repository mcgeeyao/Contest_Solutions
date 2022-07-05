

import math
import random


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

# x = 20
# for i in range(500*x, 10000*x, 500*x):
#     print(i, fn4(i, x) + 2 * fn5(i, x))
def pow(a, n, mod):
    if n == 0: return 1
    if n == 1: return a % mod
    if n % 2: return a * pow(a * a, n // 2, mod) % mod
    else: return pow(a * a, n // 2, mod) % mod
def inverse_mod(a, b):
    # Extended Euclidean algorithm from wiki
    old_s, s = 1, 0
    old_t, t = 0, 1
    old_r, r = a, b
    if b == 0:
        return 1, 0, a
    else:
        while (r != 0) :
            q = old_r // r
            old_r, r = r, old_r - q * r
            old_s, s = s, old_s - q * s
            old_t, t = t, old_t - q * t
    return old_s % b
four = 229+37+69+299+489+389
pc = 185+39+179+125+180+108
pan = 80-13+108
taung = 37+108+123
gon = 2431+59+909+514
tol = pc + pan + taung + gon
print('他們 : ', four)
print('一人', four//4)
print('pc : ', pc + four//4)
print('pan : ', pan + four//4)
print('taung : ',taung + four//4)
print('gon : ', gon)
print('tol : ', tol)