import sys
input = sys.stdin.readline
def sol(n, arr):
    d = set()
    for i in range(n):
        if arr[i] != i:
            d.add(i)
            d.add(arr[i])
    res = 2**25 - 1
    for i in d:
        res &= i
    return res
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(n, arr))