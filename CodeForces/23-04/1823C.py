import sys
input = sys.stdin.readline
from collections import defaultdict
rand = (1 << 32) - (1 << 28) - (1 << 27) - (1 << 15) - (1 << 9)
def sol(arr, n):
    mx = max(arr)
    prime = [-1] * (mx + 1)
    for i in range(2, mx + 1):
        if prime[i] != -1: continue
        prime[i::i] = [i] * ((mx)//i)
    d = defaultdict(int)
    for i in arr:
        while i != prime[i]:
            d[prime[i] ^ rand] += 1
            i //= prime[i]
        d[prime[i] ^ rand] += 1
    
    res = 0
    one = 0
    for i in d:
        res += d[i] // 2
        one += d[i] % 2
        if one == 3:
            res += 1
            one = 0
    return res
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
