import sys
input = sys.stdin.readline
def pow(x, a, mod):
    if a == 0:
        return 1
    if a == 1:
        return x % mod
    if a % 2:
        return (x * pow(x * x, a // 2, mod)) % mod
    else:
        return (pow(x * x, a // 2, mod)) % mod

def sol(n, a, b, d):
    vis = [False] * n
    
    aind = [0] * n
    for i in range(n):
        aind[a[i]] = i
    res = 0
    for i in range(n):
        if vis[a[i]]: continue
        if a[i] == b[i]: continue
        
        count = 0
        vis[a[i]] = True
        curr = i
        count += d[curr]
        while not vis[b[curr]]:
            vis[b[curr]] = True
            curr = aind[b[curr]]
            count += d[curr]
        if not count:
            res += 1

    return pow(2, res, (10 ** 9 +7))

    
t = int(input())
for case in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    d = list(map(int,input().split()))
    a = [i-1 for i in a]
    b = [i-1 for i in b]
    print(sol(n, a, b, d))
    