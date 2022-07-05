
def log(i, k):
    if i == 0:
        return 10 ** 20
    res = 0
    while i%k == 0:
        i //= k
        res += 1
    return res
n = int(input())
grid = []
check = False
for i in range(n):
    grid.append(list(map(int, input().split())))
    for j in range(n):
        if grid[i][j] == 0:
            check=True
            x0 = i
            y0 = j
dp2 = [[0]*n for _ in range(n)]
dp5 = [[0]*n for _ in range(n)]
T5 = [[-1]*n for _ in range(n)]
T2 = [[-1]*n for _ in range(n)]

dp2[0][0] = log(grid[0][0], 2)

dp5[0][0] = log(grid[0][0], 5)

for i in range(1, n):
    dp2[i][0] = dp2[i-1][0] + log(grid[i][0], 2)
    dp5[i][0] = dp5[i-1][0] + log(grid[i][0], 5)
    T5[i][0] = 1
    T2[i][0] = 1
for j in range(1, n):
    dp2[0][j] = dp2[0][j-1] + log(grid[0][j], 2)
    dp5[0][j] = dp5[0][j-1] + log(grid[0][j], 5)
    T5[0][j] = 0
    T2[0][j] = 0

for i in range(1, n):
    for j in range(1, n):
        dp2[i][j] = min(dp2[i-1][j], dp2[i][j-1]) + log(grid[i][j], 2)
        if dp2[i-1][j] < dp2[i][j-1]:
            T2[i][j] = 1
        else:
            T2[i][j] = 0
                
        dp5[i][j] = min(dp5[i-1][j], dp5[i][j-1]) + log(grid[i][j], 5)
        if dp5[i-1][j] < dp5[i][j-1]:
            T5[i][j] = 1
        else:
            T5[i][j] = 0

if dp5[n-1][n-1] < dp2[n-1][n-1]:
    if check and dp5[n-1][n-1] > 1:
        print(1)
        print("D"*x0 + "R"*y0 + "D"*(n-1-x0) + "R"*(n-1-y0))
    else:
        res = ''
        x = n-1
        y = n-1
        while T5[x][y] != -1:
            if T5[x][y] == 0:
                res+="R"
                y -= 1
            elif T5[x][y] == 1:
                res += "D"
                x -= 1
        print(dp5[n-1][n-1])
        print(res[::-1])
else:
    if check and dp2[n-1][n-1] > 1:
        print(1)
        print("D"*x0+"R"*y0+"D"*(n-1-x0)+"R"*(n-1-y0))
    else:
        res = ''
        x = n-1
        y = n-1
        while T2[x][y] != -1:
            if T2[x][y] == 0:
                res += "R"
                y -= 1
            elif T2[x][y] == 1:
                res += "D"
                x -= 1
        print(dp2[n-1][n-1])
        print(res[::-1])