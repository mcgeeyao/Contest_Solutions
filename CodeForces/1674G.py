import sys
from collections import defaultdict
n, m = tuple(map(int,input().split()))
adj = defaultdict(list)
indg = [0] * n
outdg = [0] * n
dp = [1] * n
vis = set()
finish = []

def dfs(u):
    vis.add(u)
    for v in adj[u]:
        if v not in vis:
            dfs(v)
    finish.append(u)

for _ in range(m):     
    u, v = tuple(map(int,input().split()))
    u -= 1
    v -= 1
    adj[u].append(v)
    indg[v] += 1
    outdg[u] += 1
    
for i in range(n):
    if i not in vis:
        stk = [i] 
        while stk:
            u = stk.pop()
            if u in vis:
                finish.append(u)
                continue
            vis.add(u)
            stk.append(u)
            for v in adj[u]:
                if v not in vis:
                    stk.append(v)         
res = 1
for i in finish:
    if outdg[i] > 1:
        for v in adj[i]:
            if indg[v] > 1:
                dp[i] = max(dp[i], dp[v] + 1)
        res = max(res, dp[i])
                
print(res)