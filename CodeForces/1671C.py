
t=int(input())
for case in range(t):
    n,k=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    arr.sort()
    for i in range(1,n):
        arr[i]+=arr[i-1]
    res=0
    for i in range(n):
        if k>=arr[i]:
            res+=(k-arr[i])//(i+1)+1
    print(res)