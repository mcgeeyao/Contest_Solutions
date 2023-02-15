import sys
input = sys.stdin.readline
def sol(arr, n):
    res = arr[-1] - arr[0]
    for i in range(1, n):
        res = max(res, arr[i-1] - arr[i])
    res = max(res, max(arr) - arr[0])
    res = max(res, arr[-1] - min(arr))
    return res
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
