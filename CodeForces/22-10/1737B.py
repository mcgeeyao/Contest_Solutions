from re import L
import sys
input = sys.stdin.readline

def sqrt(n):
    l = 0
    r = n
    while l <= r:
        mid = (l + r) // 2
        if mid * mid <= n: l = mid + 1
        else: r = mid - 1
    return r

def sol(n, m):
    r = sqrt(m)
    r2 = r * r
    l = sqrt(n)
    l2 = l * l
    res = (r - l) * 3
    res += (m - r2) // r
    res -= (n - 1 - l2) // l
    return res
    
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    print(sol(n, m))
