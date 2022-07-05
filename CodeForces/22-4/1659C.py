t=int(input())
for case in range(t):
    n,a,b=list(map(int,input().split()))
    l=list(map(int,input().split()))
    if n==1:
        print(l[0]*b) 
        continue
    prefix_sum=list(l)
    for i in range(n-2,-1,-1):
        prefix_sum[i]+=prefix_sum[i+1]
    curr=0
    res=prefix_sum[0]*b
    
    
    curr+=(b+a)*(l[0]-0)
    tmp=curr
    tmp+=(prefix_sum[1]-(n-1)*l[0])*b
    res=min(res,tmp)
    
    
    for i in range(1,n-1):
        curr+=(b+a)*(l[i]-l[i-1])
        tmp=curr
        tmp+=(prefix_sum[i+1]-(n-i-1)*l[i])*b
        res=min(res,tmp)
    print(res)
        
        
        
    