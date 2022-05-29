import sys
input = sys.stdin.readline

def check(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True
def sol(arr, n, m):
    no = []
    check = [False] * n
    for i in range(n):
        s = sorted(arr[i])
        dif = []
        for j in range(m):
            if s[j] != arr[i][j]:
                dif.append(j)
        if len(dif) > 2:
            return -1
        if dif:
            check[i] = True
            no.append(dif)
        else:
            no.append(None)
    ind = 0
    while ind < n and not no[ind]:
        ind += 1
    if ind == n:
        return '1 1'
    a = no[ind][0]
    b = no[ind][1]
    for i in range(n):
        if check[i]:
            if no[i][0] != a or no[i][1] != b:
                return -1
        else:
            if arr[i][a] != arr[i][b]:
                return -1
    return str(a+1) + ' ' + str(b+1)
    
                
        
    
 
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    print(sol(arr, n, m))