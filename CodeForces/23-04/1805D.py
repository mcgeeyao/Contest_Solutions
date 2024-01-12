import sys
input = sys.stdin.readline
def sol(adj, n):
    q = [0]
    vis = set()
    vis.add(0)
    while q:
        nq = []
        for u in q:
            for v in adj[u]:
                if v not in vis:
                    nq.append(v)
                    vis.add(v)
        if not nq:
            a = q[0]
        q = nq
        
    q = [a]
    vis = set()
    vis.add(a)
    dis = [0] * n
    d = 1
    while q:
        nq = []
        for u in q:
            for v in adj[u]:
                if v not in vis:
                    nq.append(v)
                    dis[v] = d
                    vis.add(v)
        if not nq:
            b = q[0]
        q = nq
        d += 1
        
    q = [b]
    vis = set()
    vis.add(b)
    d = 1
    while q:
        nq = []
        for u in q:
            for v in adj[u]:
                if v not in vis:
                    nq.append(v)
                    dis[v] = max(dis[v], d)
                    vis.add(v)
        q = nq
        d += 1
        
    dis = sorted(dis)
    l = 0
    res = []
    for i in range(1, n + 1):
        while l < n and i > dis[l]:
            l += 1
        res.append(min(n, l + 1))
    for i in res:
        print(i, end=' ')
    print()
 
n = int(input())
adj = [set() for _ in range(n)]
for i in range(n - 1):
    u, v = list(map(int,input().split()))
    adj[u-1].add(v-1)
    adj[v-1].add(u-1)
    
(sol(adj, n))
