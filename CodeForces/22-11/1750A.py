import sys
input = sys.stdin.readline
def sol(arr, n):
    if arr[0] == 1: return 'YES'
    else: return 'NO'
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
