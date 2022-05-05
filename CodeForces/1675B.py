
def sol(arr, n):
    if arr[-1] < n - 1 :
        return -1
    res = 0 
    for i in range(n - 2, -1, -1):
        if arr[i+1] == 0 : return -1
        while arr[i] >= arr[i+1]:
            arr[i] //=2
            res += 1
    return res
            
    
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))