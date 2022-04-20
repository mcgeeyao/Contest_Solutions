t=int(input())
for case in range(t):
    n,m=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    arr=sorted(arr)[::-1]
    ind=arr[0]
    arr.pop()
    for i in arr:
        ind += i+1
        if ind >= m:
            break
    if ind >= m:
        print('NO')
    else:
        print('YES')
    
    