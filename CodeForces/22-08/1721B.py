import sys
input = sys.stdin.readline
def sol(n, m, sx, sy, d):
    if (n - sx <= d and m - sy <= d):
        return -1
    if (sx <= d + 1 and sy <= d + 1):
        return -1
    if sx <= d + 1 and n - sx <= d: return -1
    if sy <= d + 1 and m - sy <= d: return -1
    return m + n - 2
t = int(input())
for case in range(t):
    n, m, sx, sy, d  = list(map(int,input().split()))
    print(sol(n, m, sx, sy, d))
