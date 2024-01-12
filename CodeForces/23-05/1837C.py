import sys
input = sys.stdin.readline
def sol(s, n):
    res = []
    if s[0] == '?':
        res.append('0')
    else:
        res.append(s[0])
    for i in range(1, n):
        if s[i] == '?':
            res.append(res[-1])
        else:
            res.append(s[i])
    return ''.join(res)
 
t = int(input())
for case in range(t):
    s = input()[:-1]
    n = len(s)
    print(sol(s, n))
