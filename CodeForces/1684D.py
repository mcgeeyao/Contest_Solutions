import sys
input = sys.stdin.readline
def sol(arr, n, k):
    b = [(arr[i] + i,i) for i in range(n)]
    b = sorted(b)[::-1]
    s = set()
    for i in range(k):
        s.add(b[i][1])
    cnt = 0
    res = sum(arr)
    for i in range(n):
        if i in s:
            cnt += 1
            res -= arr[i]
        else:
            res += cnt
    return res
t = int(input())
for case in range(t):
    n, k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(sol(arr, n, k))