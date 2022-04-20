n=int(input())
arr=list(map(int,input().split()))


res=10**30
for i in range(n):
    left=0
    l=i-1
    ma=0
    while l>=0:
        tmp=ma//arr[l]+1
        ma=(ma//arr[l]+1)*arr[l]
        left+=tmp
        l-=1
        
    right=0
    r=i+1
    mi=0
    while r<n:
        tmp=(mi)//arr[r]+1
        mi=((mi)//arr[r]+1)*arr[r]
        right+=tmp
        r+=1
    res=min(res,right+left)
    
print(res)
    