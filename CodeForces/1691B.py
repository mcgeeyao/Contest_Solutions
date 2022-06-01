from collections import defaultdict
import sys
input = sys.stdin.readline
def sol(arr, n):
    d = defaultdict(list)
    ind = defaultdict(int)
    for i in range(n):
        d[arr[i]].append(i)
    res = []
    for i in range(n):
        if len(d[arr[i]]) <= 1:
            print(-1)
            return
        res.append(d[arr[i]][(ind[arr[i]]-1)%len(d[arr[i]])])
        ind[arr[i]] += 1
    for i in range(n):
        print(res[i] + 1, end=' ')
    print()

t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    (sol(arr, n))
