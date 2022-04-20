t=int(input())
for case in range(t):
    m,n=list(map(int,input().split()))
    if m==1 and n==1:
        print(0)
        continue
    if m>n:
        m,n=n,m
    if m==1 and n>=3:
        print(-1)
        continue
    if m==1 and n==2:
        print(1)
        continue
    tmp=n-m+1
    print((m-1)*2+tmp*2-2-(tmp%2==0))
    
    