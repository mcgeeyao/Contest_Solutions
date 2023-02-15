import sys
input = sys.stdin.readline
def sol(n):
    return n + 2 * (n // 2 + n // 3)
 
t = int(input())
for case in range(t):
    n = int(input())
    print(sol( n))
