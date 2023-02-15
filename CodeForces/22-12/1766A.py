import sys
input = sys.stdin.readline
def sol(n):
    tmp = n
    cnt = 0
    while tmp >= 10:
        cnt += 1
        tmp //= 10
    return cnt * 9 + tmp
t = int(input())
for case in range(t):
    n = int(input())
    print(sol(n))
