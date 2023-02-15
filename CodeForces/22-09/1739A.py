
import sys
input = sys.stdin.readline
def sol(n, m):
    return str((n+1) // 2) + ' ' + str((m+1) // 2)
 
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    print(sol(n, m))
