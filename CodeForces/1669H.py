
t=int(input())
for case in range(t):
    n,k=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    bit=[0]*31
    for i in arr:
        tmp=i
        b=0
        while tmp:
            if tmp&1:
                bit[b]+=1
            tmp>>=1
            b+=1
    for i in range(30,-1,-1):
        if n-bit[i]<=k:
            k-=n-bit[i]
            bit[i]=n
    res=0
    for i in range(31):
        if bit[i]==n:
            res+=2**i
    print(res)
            
    
    
    