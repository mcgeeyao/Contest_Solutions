import sys
input = sys.stdin.readline
def sol(arr, n):
    arr = arr[::-1]
    if arr[0] == 1:
        print('NO')
        return 
    res = []
    cnt = 0
    for i in range(1, n):
        if arr[i] == 1:
            cnt += 1
        else:
            for j in range(cnt):
                res.append(0)
            res.append(cnt)
            cnt = 0

    print('YES')
    for j in range(cnt):
        res.append(0)
    res.append(cnt)
    cnt = 0
    
    for i in res:
        print(i, end=' ')
    print()
    return 
        
    
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    (sol(arr, n))
