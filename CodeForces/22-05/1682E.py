from collections import defaultdict
import sys
input = sys.stdin.readline
# TLE
def dfs1(u, adj, path, swap, target, par):
    if u == target:
        for i in range(1, len(path)):
            swap[path[i-1]].append(path[i])
    for v,i in adj[u]:
        if v != par:
            path.append(i)
            dfs1(v, adj, path, swap, target, u)
            path.pop()
    
def dfs2(u, sadj, finish, vis):
    
    vis[u] = True
    for v in sadj[u]:
        if not vis[v]:
            dfs2(v, sadj, finish, vis)
    finish.append(u)
    
def sol(n, arr, adj, m):
    swap_adj = defaultdict(list)
    for i in range(n):
        dfs1(i, adj, [], swap_adj, arr[i], -1)
    
    finish = []
    vis = [False] * n
    for u in range(1, m + 1):
        if not vis[u]:
            dfs2(u, swap_adj, finish, vis)
            
    for i in finish[::-1]:
        print(i, end=' ')
    print()
    
    

n, m = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr = [i - 1 for i in arr]
adj = defaultdict(list)
for i in range(1, m + 1):
    u, v = list(map(int,input().split()))
    adj[u - 1].append((v - 1, i))
    adj[v - 1].append((u - 1, i))
sol(n, arr, adj, m)