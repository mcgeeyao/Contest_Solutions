import sys
input = sys.stdin.readline
from heapq import heappop, heappush
for t in range(int(input())):
    n, m = list(map(int, input().split()))
    d = {}
    D = {}
    for i in range(n):
        x, p = list(map(int, input().split()))
        d[i] = (x, p)
        if (x, p) not in D:
            D[(x, p)] = []
        D[(x, p)].append(i)
    total, count, curr = 0, 0, 0
    heap = []
    rain = sorted(d.values())
    pos = {}
    for i in range(n):
        x, p = rain[i]
        total += p - (x-curr)*count
        count += 1
        heappush(heap, x+p)
        curr = x
        pos[curr] = total
        if i == n-1:
            break
        nxt, _ = rain[i+1]
        while heap and heap[0] <= nxt:
            total -= (heap[0]-curr)*count
            count -= 1
            curr = heappop(heap)
    heap = []
    total, count, curr = 0, 0, 0
    for i in range(n-1, -1, -1):
        x, p = rain[i]
        total -= (curr-x)*count
        count += 1
        heappush(heap, -(x-p))
        pos[x] += total
        if i < n-1 and rain[i+1][0] == x:
            pos[x] -= total
        curr = x
        total += p
        if i == 0:
            break
        nxt, _ = rain[i-1]
        while heap and -heap[0] >= nxt:
            total -= (heap[0]+curr)*count
            count -= 1
            curr = -heappop(heap)
    res = [0]*n
    L, R = [0]*n, [0]*n
    Mp = rain[0][0]
    Max = pos[Mp]
    for i in range(n):
        x, p = rain[i]
        if Max+(x-Mp) <= pos[x] or (Max <= m and pos[x] > m):
            Mp, Max = x, pos[x]
        if Max+(x-Mp)-p > m and Max > m:
            L[i] = 0
        else:
            L[i] = 1
    Mp = rain[-1][0]
    Max = pos[Mp]
    for i in range(n-1, -1, -1):
        x, p = rain[i]
        if Max+(Mp-x) <= pos[x] or (Max <= m and pos[x] > m):
            Mp, Max = x, pos[x]
        if Max+(Mp-x)-p > m and Max > m:
            R[i] = 0
        else:
            R[i] = 1
    for i in range(n):
        for ind in D[rain[i]]:
            if res[ind]:
                break
            res[ind] = str(L[i]&R[i])
    print(''.join(res))