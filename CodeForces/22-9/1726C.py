import sys
input = sys.stdin.readline
def sol(s, n):
    stk = []
    last = 0
    res = 1
    for i in s:
        if i == '(':
            stk.append(0)
            res += max(0, last - 1)
            last = 0
        else:
            stk.pop()
            last += 1
    res += max(0, last - 1)
    return res
 
t = int(input())
for case in range(t):
    n = int(input())
    s = input()[:-1]
    print(sol(s, n))
