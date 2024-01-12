import sys
input = sys.stdin.readline
def sol(n):
    res = [[0] * n, [0] * n]
    for i in range(n // 2):
        if i&1:
            res[i&1][i] = 2 * (n - i) - 1
            res[~i&1][-i-1] = 2 * (n - i)
            res[i&1][-i-1] = (n - i * 2) - 1
            res[~i&1][i] = (n - i * 2)
        else:
            res[i&1][i] = 2 * (n - i)
            res[~i&1][-i-1] = 2 * (n - i) -1
            res[i&1][-i-1] = (n - i * 2)
            res[~i&1][i] = (n - i * 2) - 1
    # for i in range(n):
    #     res[~i&1][i] = i + 1
    for i in range(n):
        print(res[0][i], end=' ')
    print()
    for i in range(n):
        print(res[1][i], end=' ')
    print()
        
t = int(input())
for case in range(t):
    n = int(input())
    (sol(n))
