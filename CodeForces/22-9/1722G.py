import sys
input = sys.stdin.readline
def sol(n):
    res = [i + 1 for i in range(n - 2)]
    if ((n - 1) // 2) % 2 == 0:
        res[-1] += 1
    x = 0
    for i in range(0, n - 2, 2):
        x ^= res[i]
    x += 1 << 18
    res.append(x)
    x = 0
    for i in range(1, n - 2, 2):
        x ^= res[i]
    x += 1 << 18
    res.append(x)
    ret = ''
    for i in res:
        ret += str(i) + ' '
    return ret
    
t = int(input())
for case in range(t):
    n = int(input())
    print(sol(n))