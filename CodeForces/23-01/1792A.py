import sys
input = sys.stdin.readline
def sol(arr, n):
    cnt = 0
    for i in arr:
        if i == 1: cnt += 1
    return n - cnt // 2    
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
