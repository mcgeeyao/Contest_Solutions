import sys
input = sys.stdin.readline
def sol(arr, n):
    arr2 = []
    for i in range(n):
        arr2.append((arr[i][0], 0, i))
        arr2.append((arr[i][1], 1, i))
    arr2.sort()
    cnt = 0
    empt = []
    res = [0] * n
    for i, j, k in arr2:
        if j == 0:
            if not empt:
                cnt += 1
                res[k] = cnt
            else:
                res[k] = empt.pop()
        else:
            empt.append(res[k])
    
    print(cnt)
    for i in range(n):
        print(res[i], end=' ')
    print()
        
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
(sol(arr, n))
