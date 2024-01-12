import sys
input = sys.stdin.readline
def sol(arr, n, m):
    cnt = 0
    for i in range(n):
        if arr[i] % m != (i + 1) % m:
            cnt += 1
    if cnt == 0:
        return 0
    if cnt == 2:
        return 1
    return -1
 
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(sol(arr, n, m))
