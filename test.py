

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

pc = 'pc'
pp = 'pp'
gon = 'gon'
dmon = {pc:0, pp:0, gon:0}
dstr = {pc:'', pp:'', gon:''}
def add(who, what, how):
    dmon[who] += how
    dstr[who] += what + '(' + str(how) + ') + ' 

add(pp, '健保', 150)
add(pc, '健保', 150)
add(pp, '噴劑', 260)
add(pp, '老邁', 175)
add(pp, '臭臭', 160)
add(pc, '老邁', 138)
add(pp, '米澤', 145)
add(pc, '米澤', 145)
add(gon, '中華', 919)
add(pc, '優市', 42)
add(gon, '洗衣', 160)
add(pp, '優市', 111)
add(pp, '麥早', 80)
add(pc, '麥早', 78)
add(pp, 'punch', 168)
add(pc, 'punch', 168)

for i in dmon:
    print(i, ':', dstr[i][:-2], '=', dmon[i])
    

