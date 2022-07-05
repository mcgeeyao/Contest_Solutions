
def sol(arr, n):
    for i in range(n-1, 0, -2):
        if arr[i] < arr[i-1]:
            arr[i] , arr[i-1] = arr[i-1] , arr[i]
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return 'NO'
    return 'YES'
    
t=int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))