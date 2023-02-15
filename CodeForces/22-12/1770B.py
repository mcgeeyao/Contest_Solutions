import sys
input = sys.stdin.readline
def sol(n, k):
    res = []
    curr = n + 1
    for i in range(k - 1):
        curr -= 1
        res.append(curr)
    res.append(1)
    mn = 2
    for i in range(k, n, k):
        for j in range(k - 1):
            if mn < curr:
                curr -= 1
                res.append(curr)
        if mn < curr:
            res.append(mn)
            mn += 1
    for i in res[::-1]:
        print(i, end=' ')
    print()
 
t = int(input())
for case in range(t):
    n, k = list(map(int,input().split()))
    (sol(n, k))
