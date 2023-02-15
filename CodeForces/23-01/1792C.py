import sys
input = sys.stdin.readline
def sol(arr, n):
    mn = dict()
    res = n // 2
    for i in arr:
        if i - 1 not in mn:
            mn[i] = i
        else:
            mn[i] = mn[i - 1]
        res = min(res, max(mn[i] - 1, n - i))
    return res
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
