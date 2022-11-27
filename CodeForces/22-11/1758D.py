import sys
input = sys.stdin.readline
def sol(n):
    if n & 1:
        print(4 * n, end=' ')
    for i in range(n // 2 - 1):
        print(4 * n + i + 1, end=' ')
        print(4 * n - i - 1, end=' ')
    print(3 * n, end=' ')
    print(5 * n, end=' ')
    
 
t = int(input())
for case in range(t):
    n = int(input())
    (sol(n))
    