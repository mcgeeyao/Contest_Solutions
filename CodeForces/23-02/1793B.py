import sys
input = sys.stdin.readline
def sol(mx, mn):
    for i in range(mx, mn, -1):
        print(i, end=' ')
    for i in range(mn, mx):
        print(i, end=' ')
    print()
 
t = int(input())
for case in range(t):
    mx, mn = list(map(int,input().split()))
    (sol(mx, mn))
