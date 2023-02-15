import sys
input = sys.stdin.readline
def sol(n, p, q):
    pd = {}
    qd = {}
    for i in range(n):
        pd[p[i]] = i
        qd[q[i]] = i
    res = 0
    a, b = min(pd[1], qd[1]), max(pd[1], qd[1])
    res += (a * (a-1)) // 2 + a
    res += ((n-1-b) * ((n-1-b)-1)) // 2 + (n-1-b)
    res += ((b-a-1) * ((b-a-1)-1)) // 2 + (b-a-1)
    for i in range(2, n + 1):
        ta, tb = min(pd[i], qd[i]), max(pd[i], qd[i])
        if a <= ta <= b or a <= tb <= b:
            a = min(a, ta)
            b = max(b, tb)
            continue
        elif ta > b:
            res += (a + 1) * (ta - b)
        elif tb < a:
            res += (n - b) * (a - tb)
        else:
            res += (a - ta) * (tb - b)
        a = min(a, ta)
        b = max(b, tb)
    return res + 1
     
     
n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
print(sol(n, p, q))
