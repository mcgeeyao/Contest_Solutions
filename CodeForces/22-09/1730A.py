import sys
input = sys.stdin.readline
def sol(arr, n, c):
    d = [0] * 101
    s = set()
    for i in arr:
        d[i] += 1
        s.add(i)
    res = 0
    for i in s:
        res += min(d[i], c)
    return res
 
t = int(input())
for case in range(t):
    n, c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(sol(arr, n, c))
