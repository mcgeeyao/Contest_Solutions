import sys
input = sys.stdin.readline
import math
def sol(arr, n):
    res = abs(arr[0] - arr[-1])
    for i in range(n//2):
        res = math.gcd(res, abs(arr[i] - arr[-i-1]))
        
    return res
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
