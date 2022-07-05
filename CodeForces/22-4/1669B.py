from collections import defaultdict


t=int(input())
for case in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    mp=defaultdict(int)
    ch=False
    for i in arr:
        mp[i]+=1
        if mp[i]>=3:
            print(i)
            ch=True
            break   
    if not ch:
        print(-1)
