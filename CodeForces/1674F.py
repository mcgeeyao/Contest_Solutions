    
n, m, q = list(map(int,input().split()))
arr = [[0]*m for _ in range(n)]
icon = 0
for i in range(n):
    tmp = input()
    for j in range(m):
        if tmp[j] == '*':
            arr[i][j] = 1
            icon += 1
            
res = 0
for i in range(icon):
    if arr[i % n][i // n] == 0:
        res += 1
   
for i in range(q):
    x, y = list(map(int,input().split()))
    if arr[x-1][y-1]:
        icon -= 1
        arr[x-1][y-1] = 0
        if x-1 + (y-1) * n > icon and arr[(icon) % n][(icon) // n] ==0 :
            res -= 1
        if x-1 + (y-1) * n < icon and arr[(icon) % n][(icon) // n]:
            res += 1
    else:
        arr[x-1][y-1] = 1
        icon += 1
        if x-1 + (y-1) * n > icon-1 and arr[(icon-1) % n][(icon-1) // n]==0:
            res += 1
        if x-1 + (y-1) * n < icon-1 and arr[(icon-1) % n][(icon-1) // n]:
            res -= 1
    print(res)
    