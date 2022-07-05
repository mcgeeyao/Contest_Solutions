import sys
input = sys.stdin.readline
def sol(n, arr):
    ind = [0] * n
    for i in range(n):
        ind[arr[i]] = i
    res = 1
    left = ind[0]
    right = ind[0]
    cnt = 0
    for i in ind[1:]:
        if left < i < right:
            res *= (right - left - cnt) % (10**9 +7)
            res %= 10**9+7
        elif i < left:
            left = i
        else:
            right = i
        cnt += 1
    return res
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(n, arr))
