# not AC
import sys
input = sys.stdin.readline
def sol(arr, n):
    pre = [0]
    for i in arr:
        pre.append(pre[-1] + i)
    dp1 = [0] * (n + 1)
    dp2 = [0] * (n + 1)
    for i in range(n - 1):
        if arr[i] > arr[i+1] - 1:
            dp1[i] = arr[i] - arr[i+1] + 1
    for i in range(n - 1, 0, -1):
        if arr[i] > arr[i-1] - 1:
            dp2[i] = arr[i] - arr[i-1] + 1
    print(dp1, dp2)
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
