import sys
from heapq import *
input = sys.stdin.readline
def sol(arr, n):
    d = {}
    for i in range(n):
        if arr[i] not in d:
            d[arr[i]] = []
        if len(d[arr[i]]) == 2: 
            print('NO')
            return 
        d[arr[i]].append(i)
    p = [0] * n
    q = [0] * n
    arr = sorted(arr, reverse=True)
    # if arr[0] != n: return 'NO'
    # if n > 1 and arr[0] == arr[1]:
    #     p[d[n][0]] = n
    #     q[d[n][1]] = n
    ind = 0
    space1 = []
    space2 = []
    for i in range(n, 0, -1):
        if i not in d:
            if not space1 or not space2:
                print('NO')
                return 
            p[space1.pop()] = i
            q[space2.pop()] = i
        elif len(d[i]) == 1:
            p[d[i][0]] = i
            q[d[i][0]] = i
        elif len(d[i]) == 2:
            p[d[i][0]] = i
            q[d[i][1]] = i
            space1.append(d[i][1])
            space2.append(d[i][0])
    print('YES')
    for i in p:
        print(i, end=' ')
    print()
    for i in q:
        print(i, end=' ')
    print()
            
        
    

t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    (sol(arr, n))
