import sys
input = sys.stdin.readline
def sol(a, b, n, m):
    
    res = 0
    if a * (m) < b * (m + 1):
        tmp = n // (m + 1)
        res += (tmp * m * a)
        res += min(a, b) * (n - tmp * (m + 1))
    else:
        res += b * n
    return res
 
t = int(input())
for case in range(t):
    a, b = list(map(int,input().split()))
    n, m = list(map(int,input().split()))
    print(sol(a, b, n, m))
