import sys
input = sys.stdin.readline
def sol(arr, n):
    K = (n+1) // 2
    dp = [[1] * K for _ in range(n)]
    
    l = 0
    while l < n-1 and arr[l] < arr[l+1]:
        l += 1
    if l == n-1:
        for i in range(n):
            print(0, end=' ')
            print()
            return 
        
    first = l + 1
    
    r = n-1
    while l >= 0 and arr[l] > arr[r]:
        l -= 1
    first = max(first, l + 1 + n - r)
    
    while r > 0 and arr[r] > arr[r-1]:
        r -= 1
        while l >= 0 and arr[l] > arr[r]:
            l -= 1
        first = max(first, l + 1 + n - r)
    
    head = [0] * n
    head[0] = 1
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            head[i] = head[i-1] + 1
        else:
            break
    tail = [0] * n
    tail[-1] = 1
    for i in range(n-2, -1, -1):
        if arr[i] < arr[i+1]:
            tail[i] = tail[i+1] + 1
        else:
            break
    
    for i in range(1, n):
        for j in range(i-1):
            if arr[j] < arr[i]:
                for k in range(1, K):
                    dp[i][k] = max(dp[i][k], dp[j][k-1] + 1)
        if arr[i-1] < arr[i]:
            for k in range(K):
                dp[i][k] = max(dp[i][k], dp[i-1][k] + 1)
                
    for i in range(k):
        print(max(dp[j][i] for j in range(n)))
                    
                    
        
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    (sol(arr, n))
