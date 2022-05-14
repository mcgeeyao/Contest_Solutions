t = int(input())
for case in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    res = 0
    for i in range(1, n):
        res += abs(max(a[i], b[i])-max(a[i-1], b[i-1]))
        res += abs(min(a[i], b[i])-min(a[i-1], b[i-1]))
    print(res)