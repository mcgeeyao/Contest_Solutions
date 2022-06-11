import sys
input = sys.stdin.readline
def sol(n):
    lastB = n&-n
    if lastB == n:
        if lastB == 1:
            return 3
        else:
            return  lastB + 1
    else:
        return lastB
 
t = int(input())
for case in range(t):
    n = int(input())

    print(sol(n))
