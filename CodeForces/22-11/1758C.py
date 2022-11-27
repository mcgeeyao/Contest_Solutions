import sys
input = sys.stdin.readline
def sol(n, m):
    if n % m != 0:
        print(-1)
        return 
    res = [i + 1 for i in range(n)]
    res[0] = m
    res[-1] = 1
    if n == m:
        for i in res:
            print(i, end=' ')
        print()
        return
    
    g = [1]
    tmp = 2
    nm = m
    while tmp * nm <= n // 2:
        while n % (tmp * nm) != 0 and tmp * nm <= n // 2:
            tmp += 1
        if tmp * nm <= n // 2:
            nm = tmp * nm
            tmp = 2
            g.append(nm // m)
        
    # for i in range(1, n // m + 1):
    #     if (i * m) > n // 2: break
    #     if n % (i * m) == 0:
    #         g.append(i)
    for i in range(len(g) - 1):
        res[m * g[i] - 1] = res[m * g[i + 1] - 1]
    if g:
        res[m * g[-1] - 1] = n
    for i in res:
        print(i, end=' ')
    print()
            
    
        
        
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    (sol(n, m))
