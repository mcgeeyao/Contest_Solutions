import sys
input = sys.stdin.readline
def sol(n):
    a = (n-2) // 3
    b = (n-2) % 3
    if b == 2 or b == 0:
        for i in range(a*3):
            print(i+1, end=' ')
        for i in range(n-2, a*3, -1):
            print(i, end=' ')
        print(n-1, n)
    elif b == 1:
        for i in range((a-1)*3):
            print(i+1, end=' ')
        for i in range(n-2, (a-1)*3, -1):
            print(i, end=' ')
        print(n-1, n)
        
 
t = int(input())
for case in range(t):
    n = int(input())
    (sol(n))
