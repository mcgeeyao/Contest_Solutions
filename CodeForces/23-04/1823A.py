import sys
input = sys.stdin.readline
def sol(n, m):
    tol = n*(n-1) // 2
    if tol == m:
        print('YES')
        print('1 ' * n)
        return 
    for i in range(n):
        tol -= n - i - 1
        tol += i
        if tol == m:
            print('YES')
            print('-1 ' * (i + 1) + '1 ' * (n - i - 1))
            return 
    print('NO')
 
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    (sol(n, m))
