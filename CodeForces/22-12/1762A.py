import sys
input = sys.stdin.readline
def sol(arr, n):
    cnt = 0
    mn = 20
    for i in range(n):
        last = arr[i] & 1
        cnt += last
        tmp = 0
        while (arr[i] & 1 == last):
            arr[i] >>= 1
            tmp += 1
        mn = min(mn, tmp)
    if cnt & 1:
        return mn
    return 0
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
