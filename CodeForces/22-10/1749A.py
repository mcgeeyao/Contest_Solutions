import sys
input = sys.stdin.readline
def sol(row, col, n):
    two = 0
    z = 0
    for i in range(n):
        if row[i] == 2:
            two += 1
        if row[i] == 0:
            z = 1
        if row[i] > 2:
            return 'NO'
    if not z: return 'NO'
    if two > 1: return 'NO'
    two = 0
    z = 0
    for i in range(n):
        if col[i] == 2:
            two += 1
        if col[i] == 0:
            z = 1
        if col[i] > 2:
            return 'NO'
    if not z: return 'NO'
    if two > 1: return 'NO'
    return 'YES'
 
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    row = [0] * n
    col = [0] * n
    for idx in range(m):
        i, j = list(map(int,input().split()))
        row[i-1] += 1
        col[j-1] += 1
    print(sol(row, col, n))
