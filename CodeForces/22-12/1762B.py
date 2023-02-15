import sys
input = sys.stdin.readline
def sol(arr, n):
    a = [(arr[i], i) for i in range(n)]
    a = sorted(a)
    curr = a[0][0]
    res = []
    for i in range(n):
        if curr < a[i][0]:
            curr = curr * ((a[i][0] // curr) + (a[i][0] % curr > 0))
        res.append((a[i][1], curr - a[i][0]))
    print(len(res))
    for i, j in res:
        print(i + 1, j)
            
            
            
            
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    (sol(arr, n))
