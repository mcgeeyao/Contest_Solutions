import sys
input = sys.stdin.readline
def sol(arr, n):
    if n & 1: return 'YES'
    for i in range(1, n - 1):
        tmp = arr[i-1] - arr[i]
        arr[i] += tmp
        arr[i + 1] += tmp
    if arr[-2] <= arr[-1]:
        return 'YES'
    else:
        return 'NO'
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
