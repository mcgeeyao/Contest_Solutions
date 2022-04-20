t=int(input())
for case in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    dp=[0]*n
    if arr[0]>0:
        dp[0]=1
    elif arr[0]==0:
        dp[0]=0
    else:
        dp[0]=-1
    for i in range(1,n):
        accu=0
        tmpres=-10**30
        for j in range(i+1):
            accu+=arr[i-j]
            if accu>0:
                tmp=j+1
            elif accu==0:
                tmp=0
            else:
                tmp=-j-1
            tmpres=max(tmpres,dp[i-j-1]+tmp)
        dp[i]=tmpres
    print(dp[-1])
    
# TLE
# should use binary indexed tree