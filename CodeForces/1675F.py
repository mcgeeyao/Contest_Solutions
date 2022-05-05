
t = int(input())
for case in range(t):
    input()
    n, k = list(map(int,input().split()))
    x, y = list(map(int,input().split()))
    x -= 1
    y -= 1
    things = list(map(int,input().split()))
    things = set([i - 1 for i in things])
    adj = [[] for _ in range(n)]
    
    for i in range(n - 1):
        u, v = list(map(int,input().split()))
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    pre = [-1] * n
    
    qu = [x]
    vis_node = set()
    vis_node.add(x)
    while qu:
        nq = []
        for i in qu:
            vis_node.add(i)
            for u in adj[i]:
                if u not in vis_node:
                    nq.append(u)
                    pre[u] = i
        qu = nq
    
    
    res = 0
    vis_node = set()
    vis_node.add(x)
    tmp = y
    while tmp not in vis_node :
        vis_node.add(tmp)
        tmp = pre[tmp]
        res += 1
    for i in things:
        tmp = i
        while tmp not in vis_node :
            vis_node.add(tmp)
            tmp = pre[tmp]
            res += 2
    print(res)