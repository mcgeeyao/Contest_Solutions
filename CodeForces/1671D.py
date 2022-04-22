
t=int(input())
for case in range(t):
    n,k=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    if n==1:
        print(max(k,arr[0])-1)
        continue
    ma=max(arr) 
    mi=min(arr)  
    diffk=10**15
    diff1=10**15
    diff1=min(diff1,arr[0]-1)
    diff1=min(diff1,arr[-1]-1)
    diffk=min(diffk,abs(arr[0]-k))
    diffk=min(diffk,abs(arr[-1]-k))
    if mi>=k:
        res=0
        for i in range(1,n):
            res+=abs(arr[i]-arr[i-1])
            diff1=min(diff1,max(0,arr[i]-2+arr[i-1]-abs(arr[i]-arr[i-1])))
        print(res+diff1)
        
    else:
        res=0
        for i in range(1,n):
            res+=abs(arr[i]-arr[i-1])
            diff1=min(diff1,max(0,arr[i]-2+arr[i-1]-abs(arr[i]-arr[i-1])))
            diffk=min(diffk,max(0,abs(arr[i]-k)+abs(arr[i-1]-k)-abs(arr[i]-arr[i-1])))
        print(res+diff1+diffk)