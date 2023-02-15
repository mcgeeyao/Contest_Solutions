from collections import defaultdict
import sys
input = sys.stdin.readline
def sol(adj, n):
    q = [1]
    cnt = 1
    vis = [False] * (n + 1)
    vis[1] = True
    while q:
        tmp = []
        m = 2
        for i in q:
            vis[i] = True
            tt = 0
            for j in adj[i]:
                if not vis[j]:
                    tt += 1
                    tmp.append(j)
            m = min(m, tt)
        if m == 1:
            return n - cnt * 2 
        if m == 0:
            return n - cnt * 2 + 1
        q = tmp
        cnt += 1
                
t = int(input())
for case in range(t):
    n = int(input())
    adj = defaultdict(list)
    for i in range(n - 1):
        u, v = list(map(int,input().split()))
        adj[u].append(v)
        adj[v].append(u)
    print(sol(adj, n))
