import sys
input = sys.stdin.readline
def sol(arr, n, k):
    d = [0] * k
    for i in range(n):
        d[i%k] = max(d[i%k], arr[i])
    return sum(d)
 
t = int(input())
for case in range(t):
    n, k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(sol(arr, n, k))
