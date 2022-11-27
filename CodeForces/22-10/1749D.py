import sys
input = sys.stdin.readline
mod = 998244353

def isPrm(n):
    i = 2
    while i * i <= n:
        if (n % i) == 0: return False
        i += 1
    return True

def sol(n, m):
    ret = 0
    res = 1
    curr = 1
    for i in range(1, n + 1):
        if isPrm(i):
            curr *= i
        res *= (m // curr)
        res %= mod
        ret += pow(m, i, mod) - res
        ret %= mod
    return ret
 

n, m = list(map(int,input().split()))
print(sol(n, m))
