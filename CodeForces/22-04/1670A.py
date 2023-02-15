from collections import defaultdict


def sol(arr, n):
    
    cnt = 0
    for i in arr:
        if i < 0:
            cnt += 1
    for i in range(cnt):
        arr[i] = -abs(arr[i])
    for i in range(cnt, n):
        arr[i] = abs(arr[i])
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return 'NO'
        
    return 'YES'
    
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))