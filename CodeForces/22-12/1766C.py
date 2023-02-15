import sys
input = sys.stdin.readline
def sol(n, a, b):
    wall = [a, b]
    ind = 0
    check = True
    for i in range(n):
        if wall[ind][i] != 'B':
            check = False
            break
        else:
            if wall[ind ^ 1][i] == 'B':
                ind ^= 1
    if check: return 'YES'
    ind = 1
    check = True
    for i in range(n):
        if wall[ind][i] != 'B':
            check = False
            break
        else:
            if wall[ind ^ 1][i] == 'B':
                ind ^= 1
    if check: return 'YES'
    else: return 'NO'
    
    
 
t = int(input())
for case in range(t):
    n = int(input())
    a = input()
    b = input()
    print(sol(n, a, b))
