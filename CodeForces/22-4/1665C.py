from  collections import defaultdict
from heapq import heapify, heappop, heappushpop,heappush

t=int(input())
for case in range(t):
    n=int(input())
    arr=[int(i) for i in input().split()]
    child=[0]*(n+1)
    for i in arr:
        child[i]+=1
    child[0]=1
    cnt=0
    for i in child:
        if i>0:cnt+=1
    res=cnt
    child.sort()
    child2=[(-child[i],(n-i)) for i in range(n+1) if child[i]>0]
    
    heapify(child2)
    while child2:
        print(child2)
        x,y=heappop(child2)
        print(res,x,y)
        time=res-y
        if time==0:
            res+=1
            if x<-2:
                heappush(child2,(x+2,res))
        elif x+time<0:
            heappush(child2,(x+time,res))
        print(res,x,y)
        print(child2)
    print(res)
    