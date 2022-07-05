import sys
input = sys.stdin.readline
def sol(n):
    if n&1:return -1
    else: return '0 ' + str(n//2) + ' ' + str(n//2)
 
t = int(input())
for case in range(t):
    n = int(input())
    print(sol(n))
