import sys
input = sys.stdin.readline
def sol(n):
    for i in range(2, n+1):
        print(i, end = ' ')
    print('1')
 
t = int(input())
for case in range(t):
    n = int(input())
    (sol(n))
