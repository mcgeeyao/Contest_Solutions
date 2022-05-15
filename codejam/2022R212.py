import sys
input = sys.stdin.readline
t = int(input())

def getMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    x, y, dx, dy = 0, 0, 1, 0
    for i in range(n*n):
        matrix[y][x] = i + 1
        if not 0 <= x + dx < n or not 0 <= y + dy < n or matrix[y+dy][x+dx] != 0:
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
    return matrix

def sol(n, k, case):
    if k % 2 or k < n - 1:
        print(f'Case #{case+1}: IMPOSSIBLE')
        return
    
    grid = getMatrix(n)
    qu = [(n//2, n//2)]
    pre = {}
    pre[(n//2, n//2)] = (-1, -1)
    dist = 1
    check = False
    first = (-1, -1)
    while qu:
        tmp = []
        for x, y in qu:
            for xx, yy in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1,y)]:
                if 0 <= xx < n and 0 <= yy < n and grid[xx][yy] < grid[x][y]:
                    if dist + grid[xx][yy] - 1 == k:
                        pre[(xx, yy)] = (x, y)
                        first = (xx, yy)
                        check = True
                        break
                    if (xx, yy) not in pre:
                        tmp.append((xx, yy))
                        pre[(xx, yy)] = (x, y)
            if check:
                break
        if check:
            break
        qu = tmp
        dist += 1
    
    res = []
    cnt = 0
    tmpx = first[0]
    tmpy = first[1]
    while  tmpx != n//2 or tmpy != n//2:
        px, py = pre[(tmpx, tmpy)]
        if grid[px][py] != grid[tmpx][tmpy] + 1:
            cnt += 1
            res.append((grid[tmpx][tmpy], grid[px][py]))  
        tmpx, tmpy = px, py
            
    print(f'Case #{case+1}: {cnt}')
    for a, b in res:
        print(str(a) + ' ' + str(b))
    
                    
                    
                    
            
            
    
    
        
    
    
        
        
        
    

for case in range(t):
    n, k = list(map(int, input().split()))
    sol(n, k, case)