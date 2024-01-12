import sys
input = sys.stdin.readline
def sol(n, a, b):
    a = sorted(a)
    b = sorted(b)[::-1]
    
    res = 1
    cnt = 0
    for i in b:
        while a and a[-1] > i:
            a.pop()
            cnt += 1
        res *= cnt
        res %= 10**9+7
        cnt -= 1
    return res
    
 
t = int(input())
for case in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(sol(n, a, b))
