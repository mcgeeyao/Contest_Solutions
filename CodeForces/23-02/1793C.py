import sys
input = sys.stdin.readline
def sol(arr, n):
    l = 0
    r = n - 1
    mn = 1
    mx = n
    while l <= r:
        if arr[l] == mn:
            mn += 1
            l += 1
        elif arr[l] == mx:
            mx -= 1
            l += 1
        elif arr[r] == mn:
            mn += 1
            r -= 1
        elif arr[r] == mx:
            mx -= 1
            r -= 1
        else:
            break
    if l <= r:
        print(l, r)
    else:
        print(-1)
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    (sol(arr, n))

