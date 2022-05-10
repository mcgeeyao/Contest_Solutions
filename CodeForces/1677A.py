import sys
input = sys.stdin.readline
def sol(arr, n):
    preprocess = [0] * n
    res = 0
    dp = [0] * n
    for mid in range(n-2, 1, -1):
        tmp = 0
        for i in range(mid, 0, -1):
            if arr[i] > arr[mid + 1]:
                preprocess[i] += 1
        for j in range(mid - 1):
            tmp += preprocess[mid - j - 1]
            dp[mid-j-1] = tmp
        for k in range(0, mid-1):
            if arr[k] < arr[mid]:
                res += dp[k+1]
    return res
    
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr = [i-1 for i in arr]
    print(sol(arr, n))