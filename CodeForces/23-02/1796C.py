import sys
input = sys.stdin.readline
def sol(n, m):
    mi = 0
    tmp = n
    while tmp <= m:
        tmp *= 2
        mi += 1
    a = m // (1 << (mi-1)) - n + 1
    if mi == 1: return f'{mi} {a}'
    b = max(0, m // ((1 << (mi-2)) * 3) - n + 1) * (mi-1)
    return f'{mi} {a+b}'
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    print(sol(n, m))
