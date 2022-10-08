import sys
input = sys.stdin.readline
def sol(n, r1 , c1, r2, c2, r3, c3, r, c):
    arr = sorted([(r1, c1), (r2, c2), (r3, c3)])
    if arr[0] == (1, 1) and arr[1] == (1, 2) and arr[2] == (2, 1):
        return r == 1 or c == 1
    if arr[0] == (n - 1, 1) and arr[1] == (n, 1) and arr[2] == (n, 2):
        return r == n or c == 1
    if arr[0] == (n - 1, n) and arr[1] == (n, n - 1) and arr[2] == (n, n):
        return r == n or c == n
    if arr[0] == (1, n - 1) and arr[1] == (1, n) and arr[2] == (2, n):
        return r == 1 or c == n
    
    for i in range(3):
        tmp = 0
        for j in range(3):
            tmp += abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1])
        if tmp == 2: mid = i
    res = (arr[mid][0] + arr[mid][1]) & 1
    
    if (r + c) & 1 != res: return True
    else:
        if r & 1 == arr[mid][0] & 1 and c & 1 == arr[mid][1] & 1: return True
    return False
 
 
t = int(input())
for case in range(t):
    n = int(input())
    r1, c1, r2, c2, r3, c3 = list(map(int,input().split()))
    r, c = list(map(int,input().split()))
    if (sol(n, r1 , c1, r2, c2, r3, c3, r, c)):
        print('YES')
    else:
        print('NO')
