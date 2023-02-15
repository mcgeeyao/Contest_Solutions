import sys
input = sys.stdin.readline
def sol(arr, n, k):
    curr = 1
    cnt = 0
    for i in arr:
        if i != curr:
            cnt += 1
        else:
            curr += 1
    return cnt // k + (cnt % k > 0)

 
t = int(input())
for case in range(t):
    n, k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(sol(arr, n, k))
