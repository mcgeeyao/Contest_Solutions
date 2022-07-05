from collections import defaultdict
import sys
input = sys.stdin.readline
def sol(n, arr):
    res = 0
    s = defaultdict(int)
    for i in arr:
        s[i] += 1
    for i, j in s.items():
        res += min(2, j)
    
    return (res + 1) // 2

t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(n, arr))