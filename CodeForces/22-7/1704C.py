import sys
input = sys.stdin.readline
from heapq import heappop, heappush
def sol(arr, n, m):
    hp = []
    arr = sorted(arr)
    for i in range(1, m):
        heappush(hp, -(arr[i] - arr[i-1] - 1))
    heappush(hp, -(n - arr[-1] + arr[0] - 1))
    res = 0
    cnt = 0
    while True:
        if not hp:
            return n - res
        tmp = heappop(hp)
        tmp = -tmp
        if tmp - 4*cnt - 1 > 0:
            res += tmp - 4*cnt - 1
        elif tmp - 4*cnt - 1 == 0:
            res += 1
        else:
            return n - res
        cnt += 1
 
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(sol(arr, n, m))
