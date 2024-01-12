import sys
input = sys.stdin.readline
def sol(n, k):
    l = 0
    r = n-1
    res = 0
    while l < r:
        res += 2
        l += k
        r -= k
    return res - (r <= l - k) + 1
 
t = int(input())
for case in range(t):
    n, k = list(map(int,input().split()))
    print(sol(n, k))
