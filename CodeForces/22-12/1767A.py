import sys
input = sys.stdin.readline
def sol(x1, x2, x3, y1, y2, y3):
    if len({x1, x2, x3}) == 2 and len({y1, y2, y3}) == 2:
        return 'NO'
    return 'YES'
 
t = int(input())
for case in range(t):
    a = input()
    x1, y1 = list(map(int, input().split()))
    x2, y2 = list(map(int, input().split()))
    x3, y3 = list(map(int, input().split()))
    print(sol(x1, x2, x3, y1, y2, y3))
