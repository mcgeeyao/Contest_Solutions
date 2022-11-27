import sys
input = sys.stdin.readline
def sol(arr, n):
    if arr[0] == min(arr):
        return 'Bob'
    else:
        return 'Alice'
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
