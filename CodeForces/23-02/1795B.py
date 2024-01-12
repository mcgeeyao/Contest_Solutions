import sys
input = sys.stdin.readline
def sol(arr, n):
    pass
 
t = int(input())
for case in range(t):
    n, k = list(map(int,input().split()))
    s1 = set()
    s2 = set()
    for i in range(n):
        x, y = list(map(int,input().split()))
        s1.add(x)
        s2.add(y)
    if k in s1 and k in s2:
        print("YES")
    else:
        print('NO')
