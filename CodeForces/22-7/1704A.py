import sys
input = sys.stdin.readline
def sol(a, b, n, m):
    if b[1:] == a[-m:] and b[0] in a[:n-m+1]: return 'YES'
    return 'NO'
 
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    a = input()
    b = input() 
    print(sol(a, b, n, m))
