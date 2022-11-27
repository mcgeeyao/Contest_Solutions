import collections
import sys
input = sys.stdin.readline
def sol(arr, n, m, q):
    xor = [0]
    curr = 0
    for i in arr:
        curr ^= i
        xor.append(curr)
    pre = [0]
    curr = 0
    for i in arr:
        curr += i
        pre.append(curr)
    qd = collections.defaultdict(list)
    for i in range(m):
        qd[q[i][1]].append((q[i][0], i))
    
    
    res = [-1] * m
    last = [collections.defaultdict(int), collections.defaultdict(int)]
    for r in range(1, n + 1):
        last[r & 1][xor[r]] = r
        for l, i in qd[r]:
            if xor[r] ^ xor[l - 1] != 0: 
                res[i] = -1
            elif pre[r] == pre[l - 1]: 
                res[i] = 0
            elif (r - l) & 1 and arr[l - 1] and arr[r - 1]:
                if last[(r & 1) ^ 1][xor[r]] >= l:
                    res[i] = 2
                else:
                    res[i] = -1
            else: 
                res[i] = 1
    
    for i in res:
        print(i)


n, m = list(map(int,input().split()))
arr = list(map(int,input().split()))
q = []
for i in range(m):
    q.append(list(map(int,input().split())))
(sol(arr, n, m, q))
