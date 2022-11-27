import sys
input = sys.stdin.readline
def sol(a, b, n):
    return sum(a) + sum(b) - max(b)
    
 
t = int(input())
for case in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(sol(a, b, n))
