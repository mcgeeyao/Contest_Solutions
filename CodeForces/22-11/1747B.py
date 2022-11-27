import sys
input = sys.stdin.readline
def sol(n):
    l = 2
    r = n * 3
    res = []
    while l < r:
        res.append((l, r))
        l += 3
        r -= 3
    print(len(res))
    for i, j in res:
        print(i, j)
    
        
 
t = int(input())
for case in range(t):
    n = int(input())
    sol(n)