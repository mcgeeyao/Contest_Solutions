import sys
input = sys.stdin.readline
def sol(g, m, n):
    dp1 = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp1[i][j] = g[i][j]
            elif i == 0:
                if dp1[i][j - 1]:
                    dp1[i][j] = dp1[i][j - 1] + 1
                else:
                    dp1[i][j] = 0
            elif j == 0:
                if dp1[i - 1][j]:
                    dp1[i][j] = dp1[i - 1][j] + 1
                else:
                    dp1[i][j] = 0
            else:
                if dp1[i - 1][j]:
                    dp1[i][j] = dp1[i - 1][j] + 1
                if dp1[i][j - 1]:
                    dp1[i][j] = max(dp1[i][j - 1] + 1, dp1[i][j])
            if g[i][j]:
                dp1[i][j] = max(dp1[i][j], 1)
                    
    dp2 = [[0] * n for i in range(m)]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:
                dp2[i][j] = g[i][j]
            elif i == m - 1:
                if dp2[i][j + 1]:
                    dp2[i][j] = dp2[i][j + 1] + 1
                else:
                    dp2[i][j] = 0
            elif j == n - 1:
                if dp2[i + 1][j]:
                    dp2[i][j] = dp2[i + 1][j] + 1
                else:
                    dp2[i][j] = 0
            else:
                if dp2[i + 1][j]:
                    dp2[i][j] = dp2[i + 1][j] + 1
                if dp2[i][j + 1]:
                    dp2[i][j] = max(dp2[i][j + 1] + 1, dp2[i][j])
            if g[i][j]:
                dp2[i][j] = max(dp2[i][j], 1)
                    
    dp3 = [[0] * n for i in range(m)]
    for i in range(m - 1, -1, -1):
        for j in range(n):
            if i == m - 1 and j == 0:
                dp3[i][j] = g[i][j]
            elif i == m - 1:
                if dp3[i][j - 1]:
                    dp3[i][j] = dp3[i][j - 1] + 1
                else:
                    dp3[i][j] = 0
            elif j == 0:
                if dp3[i + 1][j]:
                    dp3[i][j] = dp3[i + 1][j] + 1
                else:
                    dp3[i][j] = 0
            else:
                if dp3[i + 1][j]:
                    dp3[i][j] = dp3[i + 1][j] + 1
                if dp3[i][j - 1]:
                    dp3[i][j] = max(dp3[i][j - 1] + 1, dp3[i][j])
            if g[i][j]:
                dp3[i][j] = max(dp3[i][j], 1)
    dp4 = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n - 1, -1, -1):
            if i == 0 and j == n - 1:
                dp4[i][j] = g[i][j]
            elif i == 0:
                if dp4[i][j + 1]:
                    dp4[i][j] = dp4[i][j + 1] + 1
                else:
                    dp4[i][j] = 0
            elif j == n - 1:
                if dp4[i - 1][j]:
                    dp4[i][j] = dp4[i - 1][j] + 1
                else:
                    dp4[i][j] = 0
            else:
                if dp4[i - 1][j]:
                    dp4[i][j] = dp4[i - 1][j] + 1
                if dp4[i][j + 1]:
                    dp4[i][j] = max(dp4[i][j + 1] + 1, dp4[i][j])
            if g[i][j]:
                dp4[i][j] = max(dp4[i][j], 1)

    # print(dp1)
    # print(dp2)
    # print(dp3)
    # print(dp4)
    minmax = m + n + 1
    x = 0
    y = 0
    for i in range(m):
        for j in range(n):
            if max(dp1[i][j], dp2[i][j], dp3[i][j], dp4[i][j]) < minmax:
                minmax = max(dp1[i][j], dp2[i][j], dp3[i][j], dp4[i][j])
                x = i + 1
                y = j + 1
    return str(x) + ' ' + str(y)
    
 
t = int(input())
for case in range(t):
    m, n = list(map(int,input().split()))
    g = [[0] * n for i in range(m)]
    for i in range(m):
        s = input()
        for j in range(n):
            if s[j] == 'B':
                g[i][j] = 1
    
    print(sol(g, m, n))
