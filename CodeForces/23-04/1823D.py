import sys
input = sys.stdin.readline
def sol(n, m, x, c):
    res = 'abc'
    r = 0
    last = 3
    alph = 'defghijklmnopqrstuvwxyz'
    curr = 0
    curr2 = 0
    abc = 'abc'
    for i in range(m):
        tmp = x[i] - c[i]
        if tmp < r:
            return 'NO'
        a = tmp - r
        r = tmp
        for j in range(a):
            res += abc[curr2]
            curr2 = (curr2 + 1) % 3
        for j in range(x[i] - last - a):
            res += alph[curr]
        curr += 1
        last = x[i]
    for j in range(n - last):
        res += alph[curr]
    return f'YES\n{res}'
 
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    x = list(map(int,input().split()))
    c = list(map(int,input().split()))
    
    print(sol(n, m, x, c))
