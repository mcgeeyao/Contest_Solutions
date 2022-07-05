import sys
input = sys.stdin.readline
    
def sol(n, m):
    res1 = ''
    res2 = ''
    state = 0
    for i in range(m//2):
        if state:
            res1 += ' 0 1'
            res2 += ' 1 0'
        else:
            res1 += ' 1 0'
            res2 += ' 0 1'
        state = -(state-1)
    state = 0
    for i in range(n//2):
        if state:
            print(res1)
            print(res2)
        else:
            print(res2)
            print(res1)
        state = -(state-1)
    
 
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    (sol(n, m))