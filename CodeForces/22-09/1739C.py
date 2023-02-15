import sys
input = sys.stdin.readline
mod = 998244353
def pow(x, n, mod = mod):
    res = 1
    while n:
        if n & 1: res = res * x
        res %= mod
        x *= x
        x %= mod
        n >>= 1
    return res

def c(n, m, mod = mod):
    res = 1
    for i in range(n, m, -1):
        res *= i
        res %= mod 
    for i in range(1, n - m + 1):
        res *= pow(i, mod - 2)
        res %= mod 
    return res
        
dp1 = [0] * 65
dp2 = [0] * 65
dp1[2] = 1
dp2[2] = 0
for i in range(4, 64, 2):
    dp1[i] = (dp2[i - 2] + c(i - 1, i // 2 - 1)) % mod
    dp2[i] = (dp1[i - 2] + c(i - 2, i // 2 - 2)) % mod
def sol(n):
    return str(dp1[n]) + ' ' + str(dp2[n]) + ' 1'
 
t = int(input())
for case in range(t):
    n = int(input())
    print(sol(n))
