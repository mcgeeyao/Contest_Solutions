
def sol(arr,n):
    l = 0
    r = n-1
    res = 0
    pre = 0
    while l <= r:
        if arr[r] < arr[l]:
            if arr[r] >= pre:
                pre = arr[r]
                res+=1
            r-=1
        else:
            if arr[l] >= pre:
                pre = arr[l]
                res+=1
            l+=1
            
        
    return res

t=int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f'Case #{case+1}: {sol(arr,n)}')