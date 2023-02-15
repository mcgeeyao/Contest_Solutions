import sys
input = sys.stdin.readline
def sol(arr, n, x):
    mx = arr[0]
    mn = arr[0]
    res = 0
    for i in range(1, n):
        mx = max(mx, arr[i])
        mn = min(mn, arr[i])
        if mx-mn > 2*x:
            res += 1
            mx = arr[i]
            mn = arr[i]
    return res
 
t = int(input())
for case in range(t):
    n, x = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(sol(arr, n, x))
