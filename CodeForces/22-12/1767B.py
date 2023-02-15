import sys
input = sys.stdin.readline
def sol(arr, n):
    a, arr = arr[0], arr[1:]
    arr = sorted(arr)
    for i in arr:
        if a >= i: continue
        a = (a + i + 1) // 2
    return a
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
