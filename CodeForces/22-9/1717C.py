import sys
input = sys.stdin.readline
def sol(a, b, n):
    for i in range(n):
        if a[i] > b[i]: return 'NO'
        if a[i] < b[i] and b[i] > b[(i+1)%n] + 1: return 'NO'
    return 'YES'        
 
t = int(input())
for case in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(sol(a, b, n))
