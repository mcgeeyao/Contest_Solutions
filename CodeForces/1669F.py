t=int(input())

for case in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    pre=list(arr)
    post=list(arr)
    for i in range(1,n):
        pre[i]+=pre[i-1]
    for i in range(n-2,-1,-1):
        post[i]+=post[i+1]
    res=0
    l=0
    r=n-1
    while l<r:
        if pre[l]>post[r]:
            r-=1
        elif pre[l]<post[r]:
            l+=1
        else:
            if l+1+n-r>res:
                res=l+1+n-r
            l+=1
            r-=1
    print(res)
        
    