import sys
input = sys.stdin.readline
def sol(arr, n, k):
    arr.sort()
    s = sum(arr)
    pre = [0]
    for i in arr:
        pre.append(pre[-1] + i)
    res = 0
    for i in range(k+1):
        res = max(res, pre[n-i] - pre[2 * (k - i)])
    return res
 
t = int(input())
for case in range(t):
    n, k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(sol(arr, n, k))
