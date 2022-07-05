t=int(input())
a=list(map(int,input().split()))
mod=32768 
for n in a:
    best=-1
    if n==0:
        print(0,end=' ')
        continue
    n%=32768
    for i in range(16):
        tmp=(n+i)&-(n+i)
        first1=0
        while tmp:
            first1+=1
            tmp>>=1
        best=max(first1-i,best)
    print(16-best,end=' ')
    