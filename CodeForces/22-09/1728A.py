import sys
input = sys.stdin.readline
def sol(arr, n):
    mx = 0
    res = 0
    for i in range(n):
        if arr[i] > mx:
            mx = arr[i]
            res = i
    return res + 1
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
