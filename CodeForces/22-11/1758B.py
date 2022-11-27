import sys
input = sys.stdin.readline
def sol(n):
    if n & 1:
        for i in range(n):
            print(1, end = ' ')
        print()
    else:
        for i in range(n - 2):
            print(2, end = ' ')
        print(3, end = ' ')
        print(1, end = ' ')
        print()
        
 
t = int(input())
for case in range(t):
    n = int(input())
    (sol(n))
