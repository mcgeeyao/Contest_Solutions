import sys
input = sys.stdin.readline
    
def sol(arr, n):
    l = 0
    r = n - 1
    for i in range(n-1):
        if arr[i] > 0 and arr[i+1] > 0:
            return 'NO'
    while l < n and  arr[l] <= 0:
        l += 1
    while r >= 0 and arr[r] <= 0:
        r -= 1
    if r < 0:
        return 'YES'
    res = []
    while l <= r:
        acc = 0
        if arr[l] <= 0:
            while l <= r and arr[l] <= 0:
                acc += arr[l]
                l += 1
        else:
            acc = arr[l]
            l += 1
        res.append(acc)
    if len(res) <= 2:
        return 'YES'
    

    stack = [0]
    dp = [0] * len(res)
    for i in range(2, len(res), 2):
        acc = res[i-1]
        while stack and res[stack[-1]] <= res[i]:
            acc += res[stack[-1]]
            if acc > 0:return 'NO'
            acc += dp[stack.pop()]
        dp[i] = acc
        stack.append(i)
    
    stack = [len(res) - 1]
    dp = [0] * len(res)
    for i in range(len(res)- 3, -1, -2):
        acc = res[i+1]
        while stack and res[stack[-1]] <= res[i]:
            acc += res[stack[-1]]
            if acc > 0:return 'NO'
            acc += dp[stack.pop()]
        dp[i] = acc
        stack.append(i)
    return 'YES'
        

t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
