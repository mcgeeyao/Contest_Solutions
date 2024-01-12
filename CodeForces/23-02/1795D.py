import sys
input = sys.stdin.readline
def sol(arr, n):
    res = 1
    mod = 998244353
    for i in range(0, n, 3):
        mx = min(arr[i], arr[i+1], arr[i+2])
        cnt = 0
        if arr[i] == mx: cnt += 1
        if arr[i+1] == mx: cnt += 1
        if arr[i+2] == mx: cnt += 1
        res *= cnt
        res %= mod
    # print(res)
        
    for i in range(n // 6 + 1, n // 3 + 1):
        res *= i
        res %= mod
    for i in range(1, n // 6 + 1):
        res *= pow(i, mod-2, mod)
        res %= mod
    return res
        
n = int(input())
arr = list(map(int,input().split()))
print(sol(arr, n))
