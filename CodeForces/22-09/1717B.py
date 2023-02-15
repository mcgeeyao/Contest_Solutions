import sys
input = sys.stdin.readline
def sol(n, k ,r, c):
    r -= 1
    c -= 1
    res = [['.'] * n for _ in range(n)]
    for i in range(n//k):
        for j in range(n//k):
            for l in range(k):
                res[i*k + l][j*k + l] = 'X'
    if abs(r-c) % k:
        rr2 = r%k
        cc2 = c%k
        for i in range(n//k):
            for j in range(n//k):
                res[i*k + rr2][j*k + cc2] = 'X'
                res[i*k + rr2][j*k + rr2] = '.'
                res[i*k + cc2][j*k + cc2] = '.'
                res[i*k + cc2][j*k + rr2] = 'X'
    for i in range(n):
        for j in range(n):
            print(res[i][j], end='')
        print()
        
t = int(input())
for case in range(t):
    n, k ,r, c = list(map(int,input().split()))
    (sol(n, k ,r, c))
