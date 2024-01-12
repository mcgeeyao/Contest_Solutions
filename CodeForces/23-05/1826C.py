import sys
input = sys.stdin.readline
tol = (10**6+5)
p = [-1] * tol
for i in range(2, tol):
    if p[i] != -1: continue
    for j in range(i, tol, i):
        p[j] = i
p[1] = 1
def sol(n, m):
    if n == 1: return 'YES'
    s = set()
    while p[n] != n:
        s.add(p[n])
        n //= p[n]
    s.add(p[n])
    for i in s:
        if i <= m:
            return 'NO'
        
    return 'YES'
 
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    print(sol(n, m))
