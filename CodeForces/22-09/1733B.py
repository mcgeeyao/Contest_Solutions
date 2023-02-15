import sys
input = sys.stdin.readline
def sol(n, x, y):
    if x != 0 and y != 0:
        return -1
    if x == 0 and y == 0:
        return -1
    if x == 0:
        tmp = y
    else:
        tmp = x
    if (n-1) % tmp != 0: return -1
    res = '1 ' * tmp
    for i in range(1, (n-1)//tmp):
        res += (str(2 + (i) * tmp) + ' ') * tmp
    return res
        
    
 
t = int(input())
for case in range(t):
    n, x, y = list(map(int,input().split()))
    print(sol(n, x, y))
