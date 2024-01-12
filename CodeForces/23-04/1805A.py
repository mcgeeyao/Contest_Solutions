import sys
input = sys.stdin.readline
def sol(arr, n):
    b = 0
    for i in arr:
        b ^= i
    if n & 1:
        return b
    else:
        if b == 0:
            return b
        else:
            return -1
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
