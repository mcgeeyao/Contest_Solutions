import sys
input = sys.stdin.readline
from collections import defaultdict
def sol(n, lb):
    sta = sorted(lb.keys())
    res = 0
    for i in sta:
        res += sum(sorted(lb[i])[::-1][:i])
    return res
 

t = int(input())
for case in range(t):
    n = int(input())
    lb = defaultdict(list)
    for i in range(n):
        a, b = (map(int,input().split()))
        lb[a].append(b)
    print(sol(n, lb))
