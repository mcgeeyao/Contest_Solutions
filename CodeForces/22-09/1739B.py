import sys
input = sys.stdin.readline
def sol(arr, n):
    res = [arr[0]]
    for i in range(1, n):
        if arr[i] and arr[i] <= res[-1]:
            print(-1)
            return 
        res.append(res[-1] + arr[i])
    for i in res:
        print(i, end = ' ')
    print()
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    (sol(arr, n))
