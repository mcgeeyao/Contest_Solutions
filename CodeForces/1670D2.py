import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    num = int(input())

    l = 0
    r = 38730
    while l <= r :
        n = (l + r) // 2
        tmp = n*(n-1)
        res = (tmp//2 - tmp//6 + n//3)*2
        if res < num:
            l = n + 1
        else :
            r = n - 1
    print(l)