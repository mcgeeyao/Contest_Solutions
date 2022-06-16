import sys
input = sys.stdin.readline
def sol(a, b):
    if a < b:
        return '10' * a + '1' * (b - a)
    else:
        return '01' * b + '0' * (a - b)
 
t = int(input())
for case in range(t):
    a, b = list(map(int,input().split()))
    print(sol(a, b))
