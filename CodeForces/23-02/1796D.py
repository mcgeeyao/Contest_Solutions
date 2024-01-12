import sys
input = sys.stdin.readline
def sol(arr, n, k, x):
    dp = [[0] * n for _ in range(k + 1)]
    ln = [[0] * n for _ in range(k + 1)]
    a = [i-x for i in arr]
    dp[0][0] = a[0]
    ln[0][0] = 1
    for i in range(1, n):
        if dp[0][i-1] >= 0:
            ln[0][i] = ln[0][i-1] + 1
        else:
            ln[0][i] = 1
        dp[0][i] = max(0, dp[0][i-1]) + a[i]
        
    for j in range(1, k+1):
        dp[j][0] = a[0] + x + x
        for i in range(1, n):
            if ln[j-1][i] == j-1:
                if dp[j-1][i] + a[i-ln[j-1][i]] + x + x > dp[j][i]:
                    ln[j][i] = ln[j-1][i] + 1
                dp[j][i] = max(dp[j][i], dp[j-1][i] + a[i-ln[j-1][i]] + x + x)
                
            elif ln[j-1][i] > j-1:
                if dp[j-1][i] + x + x > dp[j][i]:
                    ln[j][i] = ln[j-1][i]
                dp[j][i] = max(dp[j][i], dp[j-1][i] + x + x)
                
            if ln[j][i-1] >= j:
                if dp[j][i-1] + a[i] > dp[j][i]:
                    ln[j][i] = ln[j][i-1] + 1
                dp[j][i] = max(dp[j][i], dp[j][i-1] + a[i])
                
            if ln[j][i-1] < j:
                if dp[j][i-1] + a[i] + x + x > dp[j][i]:
                    ln[j][i] = ln[j][i-1] + 1
                dp[j][i] = max(dp[j][i], dp[j][i-1] + a[i] + x + x)
    print(dp, ln)
    return max(dp[-1])
            
            
t = int(input())
for case in range(t):
    n, k, x = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(sol(arr, n, k, x))
