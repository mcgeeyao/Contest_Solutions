import sys
input = sys.stdin.readline
def sol(arr, n):
    a = 0
    b = 0
    for i in arr:
        if i < 0: a += i
        else: b -= i
    return abs(a - b)
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
