import sys
input = sys.stdin.readline
def sol(arr, n):
    if n == 1 : 
        print(-1)
        return 
    re = [i for i in range(1, n + 1)][::-1]
    res = []
    for i in range(n - 1):
        if arr[i] != re[-1]:
            res.append(re.pop())
        else:
            res.append(re.pop(-2))
    
    if arr[-1] == re[-1]:
        tmp = res[-1]
        res[-1] = re[-1]
        re[-1] = tmp
    res.append(re.pop())
    for i in res:
        print(i, end=' ')
    print()  
    return 
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    (sol(arr, n))
