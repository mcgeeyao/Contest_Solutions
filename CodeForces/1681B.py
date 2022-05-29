import sys
input = sys.stdin.readline
def sol(n, a, m, b):
    return a[sum(b)%n]
    
 
t = int(input())
for case in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    print(sol(n, a, m, b))