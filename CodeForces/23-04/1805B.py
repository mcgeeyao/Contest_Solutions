import sys
input = sys.stdin.readline
def sol(s, n):
    mn = 500
    for i in s:
        mn = min(mn, ord(i))
    for i in range(n - 1, -1, -1):
        if ord(s[i]) == mn:
            return s[i] + s[:i] + s[i + 1:]
 
t = int(input())
for case in range(t):
    n = int(input())
    s = input()[:-1]
    print(sol(s, n))
