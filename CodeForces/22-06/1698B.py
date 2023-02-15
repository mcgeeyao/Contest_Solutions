import sys
input = sys.stdin.readline
def sol(arr, n, k):
    if k == 1:
        return (n-1)//2
    res = 0
    for i in range(1, n-1):
        if arr[i] > arr[i-1] + arr[i+1]:
            res += 1
    return res
 
t = int(input())
for case in range(t):
    n, k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(sol(arr, n, k))
