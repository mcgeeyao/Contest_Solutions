import sys
input = sys.stdin.readline
from heapq import heappop, heappush
def sol(a, b, n, x, y):
    dif = []
    for i in range(n):
        if a[i] != b[i]: dif.append(i)
    l = len(dif)
    if l & 1: return -1
    if not dif: return 0
    if x >= y and l > 2: return l // 2 * y
    # res1 = 0
    # for i in range(0, l, 2):
    #     if dif[i] + 1 == dif[i + 1]:
    #         if 1 < dif[i] or dif[i] < n - 3:
    #             res1 += min(x, y + y)
    #         elif n == 4 and dif[i] == 1:
    #             res1 += min(x, y + y + y)
    #         else:
    #             res1 += x
    #     else:
    #         res1 += min(x * (dif[i + 1] - dif[i]), y)
    # if l == 2: return res1
    
    # res2 = min(y, x * (dif[-1] - dif[0]))
    # for i in range(1, l - 1, 2):
    #     if dif[i] + 1 == dif[i + 1]:
    #         if 1 < dif[i] or dif[i] < n - 3:
    #             res2 += min(x, y + y)
    #         elif n == 4 and dif[i] == 1:
    #             res2 += min(x, y + y + y)
    #         else:
    #             res2 += x
    #     else:
    #         res2 += min(x * (dif[i + 1] - dif[i]), y)
    right = [i + 1 for i in range(l)]
    right[-1] = -1
    left = [i - 1 for i in range(l)]
    
    # if x >= y: return min(res1, res2)
    
    heap = []
    for i in range(l-1):
        heappush(heap, (dif[i + 1] - dif[i], i, i + 1))
    res3 = 0
    while heap:
        d, i, j = heappop(heap)
        if right[i] != j: continue
        if dif[i] + 1 == dif[j]:
            if 1 < dif[i] or dif[i] < n - 3:
                res3 += min(x, y + y)
            elif n == 4 and dif[i] == 1 and dif[j] == 2:
                res3 += min(x, y + y + y)
            else:
                res3 += x
        else:
            res3 += min(x * (dif[j] - dif[i]), y)
        if left[i] >= 0:
            right[left[i]] = right[j]
        if right[j] >= 0:
            left[right[j]] = left[i]
        if left[i] >= 0 and right[j] >= 0:
            heappush(heap, (dif[right[j]] - dif[left[i]], left[i], right[j]))
        left[i] = -1
        left[j] = -1
        right[i] = -1
        right[j] = -1
    # return min(res1, res2, res3)
    print(left)
    return res3
t = int(input())
for case in range(t):
    n, x, y = list(map(int,input().split()))
    a = input()
    b = input()
    print(sol(a, b, n, x, y))
