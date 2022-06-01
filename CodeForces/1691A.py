import sys
input = sys.stdin.readline
def sol(arr, n):
    o = 0
    e = 0
    for i in arr:
        if i % 2:
            o += 1
        else: e += 1
    return min(o, e)
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
