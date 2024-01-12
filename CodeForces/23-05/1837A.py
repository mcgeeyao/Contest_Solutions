import sys
input = sys.stdin.readline
def sol(x, k):
    if x % k != 0:
        print(1)
        print(x)
    else:
        print(2)
        print(1, x-1)
 
t = int(input())
for case in range(t):
    x, k = list(map(int,input().split()))
    (sol(x, k))
