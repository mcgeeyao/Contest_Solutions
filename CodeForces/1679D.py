import sys
input = sys.stdin.readline
n, m, k = list(map(int,input().split()))
arr = list(map(int,input().split()))

adj = [list() for _ in range(n)]
for i in range(m):
    u, v = list(map(int,input().split()))
    adj[u-1].append(v-1)
    
# def dfs(u, vis, val, dist, group):
    
#     vis[u] = True
#     group[u] = 1
#     for v in adj[u]:
#         if arr[v] <= val :
#             if group[v]:
#                 dist[u] = 10**18
#                 return True
#             if not vis[v]:
#                 dfs(v, vis, val, dist, group)
#                 group[v] = 0
#             dist[u] = max(dist[u], dist[v] + 1)
#         if dist[u] >= k :
#             return True
                

def ok(val):
    if k == 1:return True
    vis = [False] * n
    dist = [1] * n
    group = [0] * n
    for i in range(n):
        if arr[i] <= val and not vis[i]:
            stk = [i]
            while stk:
                u = stk.pop()
                if vis[u]:
                    for v in adj[u]:
                        if arr[v] <= val :
                            dist[u] = max(dist[u], dist[v] + 1)
                            if dist[u] >= k :
                                return True
                            group[v] = 0
                    group[u] = 0
                    continue
                stk.append(u)
                group[u] = 1
                vis[u] = True
                for v in adj[u]:
                    if group[v]:
                        return True
                    if arr[v] <= val :
                        if not vis[v]:
                            stk.append(v)
    return False
            


sor = sorted(arr)
l = 0
r = n - 1
while l <= r :
    mid = (l + r) // 2
    if ok(sor[mid]):
        r = mid - 1
    else:
        l = mid + 1
if l == n:
    print(-1)
else:
    print(sor[l]) 