import sys
input = sys.stdin.readline
def dfs(u, adj, finish, vis):
    vis.add(u)
    for v in adj[u]:
        if v not in vis:
            dfs(v, adj, finish, vis)
    finish.append(u)
def sol(arr, n, m, adj, p, interval):
    mod = 998244353
    vis = set()
    finish = []
    for i in range(n):
        if i not in vis:
            dfs(i, adj, finish, vis)
    
    for i in finish[::-1]:
        interval[i] = merge_interval(interval[i])
        for nxt in adj[i]:
            for s, e in interval[i][1:]:
                interval[nxt].append([s+1, e+1])
    return interval[finish[0]][-1][-1]
    
def merge_interval(L):
    if len(L) < 2:
        return L
    L.sort()
    res = [L[0], L[1]]
    for s, e in L[2:]:
        if s <= res[-1][-1]+1:
            res[-1][-1] += e-s+1
        else:
            res.append([s, e])
    return res

MOD = 998244353
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    adj = [list() for _ in range(n)]
    p = [list() for _ in range(n)]
    interval = [[[0, 0]] for i in range(n)]
    for i in range(n):
        if arr[i] > 0:
            interval[i].append([1, arr[i]])
    for i in range(m):
        u, v = list(map(int,input().split()))
        adj[u-1].append(v-1)
        p[v-1].append(u-1)
    print(sol(arr, n, m, adj, p, interval)%MOD)