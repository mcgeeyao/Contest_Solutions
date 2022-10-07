import sys
input = sys.stdin.readline

def check(ly, p, mid, k):
    if mid == 1:
        cnt = 0
        for i in p:
            if i > 1: cnt += 1
        return cnt <= k
    n = len(ly)
    d2 = [0] * (n + 2)
    cnt = 0
    for i in range(n - 1, 0, -1):
        for j in ly[i]:
            if d2[j] >= mid - 1 and p[j-1] != 1:
                cnt += 1
            else:
                d2[p[j-1]] = max(d2[p[j-1]], d2[j] + 1)
    return cnt <= k
            


def sol(arr, n, k):
    d = [0] * (n + 2)
    ly = [list() for _ in range(n)]
    ly[0].append(1)
    for i in range(n - 1):
        d[i+2] = d[arr[i]] + 1
        ly[d[i+2]].append(i+2)
    arr = [0] + arr
    l = 1
    r = n
    while l <= r:
        mid = (l + r) // 2
        if check(ly, arr, mid, k):
            r = mid - 1
        else:
            l = mid + 1
    return l
 
t = int(input())
for case in range(t):
    n, k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(sol(arr, n, k))
