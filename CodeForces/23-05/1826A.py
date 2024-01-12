import sys
input = sys.stdin.readline
def sol(arr, n):
    arr = sorted(arr)[::-1]
    if arr[0] == 0:
        return 0
    for i in range(n):
        if arr[i] <= i and arr[i-1] > i:
            return i
    return -1
    
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
