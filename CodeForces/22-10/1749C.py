import sys
input = sys.stdin.readline
def sol(arr, n):
    arr = sorted(arr, reverse=True)
    for i in range(n // 2 + 5, 0, -1):
        tmp = i
        f = 0
        cnt = 0
        while f < n and arr[f] > tmp: f += 1
        for j in range(f, n - i + 1):
            if arr[j] <= tmp:
                cnt += 1
                tmp -= 1
        if cnt >= i:
            return i
    return 0
            
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
