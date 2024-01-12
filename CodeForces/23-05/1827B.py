import sys
input = sys.stdin.readline
from math import gcd
def sol(arr, n):
    tmp = []
    for i in range(n):
        if abs(arr[i] - 1 - i):
            tmp.append(abs(arr[i] - 1 - i))
    res = tmp[0]
    for i in tmp:
        res = gcd(res, i)
    return res
    
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
