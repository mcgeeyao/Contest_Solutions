# will TLE
import sys
input = sys.stdin.readline
def dfs(u, adj, vis, finish):
    vis.add(u)
    for v in adj[u]:
        if v not in vis:
            dfs(v, adj, vis, finish)
    finish.append(u)
def sol(arr, n, m, mx, mn):
    adj = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if mx[i] < mn[j]:
                adj[i].add(j)
            if mx[j] < mn[i]:
                adj[j].add(i)
                
    vis = set()
    finish = []
    for i in range(n):
        if i not in vis:
            dfs(i, adj, vis, finish)
    finish = finish[::-1]
    print(finish, adj)
    dp = [0] * n
    for i in finish:
        dp[i] += arr[i]
        for j in adj[i]:
            dp[j] = max(dp[j], dp[i])
    return max(dp)
    
 
m, n = list(map(int,input().split()))
arr = list(map(int,input().split()))
mx = [0] * n
mn = [10 ** 9 + 5] * n
for _ in range(m):
    tmp = list(map(int,input().split()))
    for i in range(n):
        mx[i] = max(mx[i], tmp[i])
        mn[i] = min(mn[i], tmp[i])
        
print(sol(arr, n, m, mx, mn))
