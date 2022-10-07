

import math
import random
from turtle import st
import collections


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

add(gon, '水費', 441)
add(pc, '711原萃', 50)
add(pp, '湖州八道', 105)
add(pc, '湖州八道', 105)
add(pc, '當歸鴨', 110)
add(pc, 'UE全聯', 138)
add(pp, 'UE全聯', 20)
add(pc, '景新', 105)
add(pp, '景新', 105)
add(pc, '老邁', 170)
add(pp, '老邁', 128)
add(pc, '鑫吉', 120)
add(pp, '鑫吉', 120)
add(pc, '炒飯', 120)
add(pp, '炒飯', 120)
add(pc, '湯頂鮮', 160)
add(pp, '湯頂鮮', 170)
add(pc, '老邁', 148)
add(pp, '老邁', 138)
add(pc, '岡山', 190)
add(pp, '岡山', 125)
add(pp, '印吵', 48)
add(gon, '洗碗', 79)
add(pp, '銅鑼豆漿', 137)
add(pp, '虎斑', 65)
add(pc, '虎斑', 85)
add(pp, '鯛魚', 90)
add(pc, '雞排', 90)


for i in dmon:
    print(i, ':', dstr[i][:-2], '=', dmon[i])
    
    
    
def solution(arr):
    d = [0] * 1005
    for i in arr: d[i] += 1
    pre = 0
    res = 1005
    for i in sorted(set(arr)):
        if d[i] >= 4: return 0
        if pre and d[i] >= 2: res = min(res, i - pre)
        if d[i] >= 2: pre = i
    if res == 1005: return -1
    return res

def solution(s):
    d = {'a': 0, 'b': 1, 'c':2}
    res = d[s[0]]
    for i in range(len(s) - 1): res += (d[s[i + 1]] - d[s[i]] + 2) % 3
    return res

