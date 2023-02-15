import sys
input = sys.stdin.readline
MOD = 10**9+7
def sol(n, k):
    if k == 0:
        return(1)
    if k >= n:
        return (pow(2, n, MOD))
    res = 1
    curr = 1
    for i in range(1, k+1):
        curr *= (n-i+1)
        curr //= i
        res += curr 
        res %= MOD
    return res
 
n, k = list(map(int,input().split()))
print(sol(n, k))
