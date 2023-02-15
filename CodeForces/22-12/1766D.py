import sys
input = sys.stdin.readline

primes = [-1] * 10 ** 7
for i in range(2, 10 ** 7):
    if primes[i] != -1: continue
    for j in range(i, 10 ** 7, i):
        primes[j] = i

def sol(a, b):
    dif = b - a
    if dif == 1: return -1
    if (dif & 1) == 0 and (a & 1) == 0: return 0
    res = -a % primes[dif]
    while primes[dif] != dif:
        dif //= primes[dif]
        res = min(res, -a % primes[dif])
    return res
 
t = int(input())
for case in range(t):
    a, b = list(map(int,input().split()))
    print(sol(a, b))