import sys
input = sys.stdin.readline
def sol(arr, n, k):
    if k <= n:
        sub = sum(arr[:k])
        max_sub = sub
        for i in range(k, n):
            sub += arr[i]
            sub -= arr[i - k]
            max_sub = max(max_sub, sub)
        return max_sub + (k - 1) * k // 2
    else:
        return sum(arr) + k * n - n * (n+1) // 2
    
 
t = int(input())
for case in range(t):
    n, k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(sol(arr, n, k))
