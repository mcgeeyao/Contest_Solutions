import sys
input = sys.stdin.readline
def sol(n):
    a = (n-1)*(n+2)//2
    diff = (a // n + 1) * n - a
    print(diff, end = ' ')
    for i in range(2, n + 1):
        print(i, end=' ')
    print()
 
t = int(input())
for case in range(t):
    n = int(input())
    (sol(n))
