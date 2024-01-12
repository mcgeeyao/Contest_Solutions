import sys
input = sys.stdin.readline
def sol(n, s):
    res = 1
    curr = 1
    for i in range(1, n):
        if s[i] == s[i-1]:
            curr += 1
        else:
            curr = 1
        res = max(res, curr)
    return res+1
 
t = int(input())
for case in range(t):
    n = int(input())
    s = input()[:-1]
    print(sol(n, s))

