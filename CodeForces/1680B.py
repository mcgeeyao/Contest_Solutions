import sys
input = sys.stdin.readline
def sol(m, n, grid):
    res1 = (-1, -1)
    for i in range(m):
        check = False
        for j in range(n):
            if grid[i][j]:
                res1 = (i, j)
                check = True
                break
        if check:
            break
    res2 = (-1, -1)
    for i in range(n):
        check = False
        for j in range(m):
            if grid[j][i]:
                res2 = (j, i)
                check = True
                break
        if check:
            break
    if res1 == res2:
        return 'YES'
    return 'NO'
        
     
t = int(input())
for case in range(t):
    m, n = list(map(int,input().split()))
    grid = [[0]*n for _ in range(m)]
    for i in range(m):
        tmp = input()
        for j in range(n):
            if tmp[j] == 'R':
                grid[i][j] = 1
        
    print(sol(m, n, grid))