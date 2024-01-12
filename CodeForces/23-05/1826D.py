import sys
input = sys.stdin.readline
def sol(arr, n):
    dp1 = [0] * n
    for i in range(n):
        dp1[i] = max(dp1[i-1]-1, arr[i])
    dp2 = [0] * n
    for i in range(1, n):
        dp2[i] = max(dp2[i-1]-1, arr[i] + dp1[i-1]-1)
        
    dp3 = [0] * n
    for i in range(2, n):
        dp3[i] = max(dp3[i-1]-1, arr[i] + dp2[i-1]-1)

    return max(dp3)
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
