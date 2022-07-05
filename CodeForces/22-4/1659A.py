import math
t=int(input())
for case in range(t):
    n,r,b=list(map(int,input().split()))
    tmp=math.ceil(r/(b+1))

    res=''
    while r>=tmp and r>b and b>0:
        res+='R'*tmp+"B"
        r-=tmp
        b-=1
    while r>0 and b>0:
        res+="R"+"B"
        r-=1
        b-=1
    while r>0:
        res+="R"
        r-=1
    while b>0:
        res+="B"
        b-=1
    print(res)
    