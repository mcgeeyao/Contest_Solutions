from  collections import defaultdict
t=int(input())
for case in range(t):
    n=int(input())
    arr=[int(i) for i in input().split()]
    d=defaultdict(int)
    for i in arr:
        d[i]+=1
    most=0
    for i in arr:
        if d[i]>most:
            m=i
            most=d[i]
    a=most
    b=most
    res=0
    while a<n:
        if b>a:
            tmp=(b-a)
            if n-a>=tmp:
                res+=tmp
                a+=tmp
            else:
                res+=n-a
                a=n
        else:
            b=a*2
            res+=1
    print(res)
                
    