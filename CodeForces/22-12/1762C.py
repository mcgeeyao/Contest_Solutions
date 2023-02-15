import sys
input = sys.stdin.readline
def sol(arr, n):
    res = 1
    curr = 1
    mod = 998244353 
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            curr = (curr << 1) % mod
        else:
            curr = 1
        res += curr
        res %= mod

    return res
        
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = input()[:-1]
    print(sol(arr, n))
