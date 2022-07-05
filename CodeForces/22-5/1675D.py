from collections import defaultdict


def sol(arr, n):
    adj = defaultdict(list)
    for i in range(n):
        if i + 1 != arr[i]:
            adj[arr[i] - 1].append(i)
    finish = []
    vis = set()
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
    finish = finish[::-1]
    vis1 = [False] * n
    res = []
    for i in finish:
        if not vis1[i]:
            stk = [i]
            path = []
            while stk:
                u = stk.pop()
                path.append(u)
                vis1[u] = True
                for v in adj[u]:
                    if not vis1[v]:
                        stk.append(v)
                        break
            res.append(path)
            
    print(len(res))
    for i in res:
        print(len(i))
        for j in i:
            print(j + 1, end = ' ')
        print()
    print()
            
    
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    sol(arr, n)