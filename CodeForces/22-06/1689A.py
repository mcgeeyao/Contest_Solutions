import sys
input = sys.stdin.readline
def sol(n, m, k, a, b):
    a = sorted(a)
    b = sorted(b)
    ai = 0
    bi = 0
    res = ''
    last = -1
    cnt = 0
    while ai < len(a) and bi < len(b):
        if cnt == k:
            if last == 0:
                res += b[bi]
                cnt = 1
                last = 1
                bi += 1
            else:
                res += a[ai]
                cnt = 1
                last = 0
                ai += 1
            continue
        if ord(a[ai]) < ord(b[bi]):
            res += a[ai]
            if last == 0:
                cnt += 1
            else:
                cnt = 1
                last = 0
            ai += 1
        else:
            res += b[bi]
            if last == 1:
                cnt += 1
            else:
                cnt = 1
                last = 1
            bi += 1
    return res
            
 
t = int(input())
for case in range(t):
    n, m, k = list(map(int,input().split()))
    a = input()[:-1]
    b = input()[:-1]
    
    print(sol(n, m, k, a, b))
