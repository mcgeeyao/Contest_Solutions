import sys
input = sys.stdin.readline
def sol(arr, n, m, edges):
    ecnt = [0] * n
    for i, j in edges:
        ecnt[i-1] += 1
        ecnt[j-1] += 1
    if not m&1: return 0
    res = 10**18
    for i in range(n):
        if ecnt[i]&1:
            res = min(res, arr[i])
    for i, j in edges:
        if not ecnt[i-1]&1 and not ecnt[j-1]&1:
            res = min(res, arr[i-1] + arr[j-1])
    return res
 
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    edges = []
    for i in range(m):
        edges.append(list(map(int,input().split())))
    print(sol(arr, n, m, edges))
