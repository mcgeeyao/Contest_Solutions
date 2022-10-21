import sys
input = sys.stdin.readline
mod = 998244353
def sqrt(n):
    l = 0
    r = n
    while l <= r:
        mid = (l + r) // 2
        if mid * mid <= n: l = mid + 1
        else: r = mid - 1
    return r

def isPrm(n):
    for i in range(2, sqrt(n) + 1):
        if (n % i) == 0:
            return False
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
