import sys
input = sys.stdin.readline
from collections import defaultdict
def sol(s):
    d = defaultdict(int)
    for i in s: d[i] += 1
    cnt = 0
    for i in d: 
        cnt += (d[i]>=2)
    if cnt > 1:
        return 'YES'
    else:
        return 'NO'
 
t = int(input())
for case in range(t):
    s = input()[:-1]
    print(sol(s))
