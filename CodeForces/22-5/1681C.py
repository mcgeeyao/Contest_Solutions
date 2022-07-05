import sys
input = sys.stdin.readline
def sol(n, a, b):
    sa = sorted(a)
    sb = sorted(b)
    pa = [(a[i], b[i]) for i  in range(n)]
    pa = sorted(pa)
    for i in range(n):
        if sb[i] != pa[i][1]:
            print(-1)
            return 
    cnt = 0
    res = []
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j+1] or b[j] > b[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                b[j], b[j + 1] = b[j + 1], b[j]
                res.append((j, j + 1))
                cnt += 1
    print(cnt)
    for i, j in res:
        print(i+1,j+1)
    
    
t = int(input())
for case in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    (sol(n, a, b))
