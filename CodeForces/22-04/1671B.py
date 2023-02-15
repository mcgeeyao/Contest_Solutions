
t=int(input())
for case in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    diff=[0,0]
    ch=True
    for i in range(1,n):
        if arr[i]-arr[i-1]==3:
            diff[1]+=1
        elif  arr[i]-arr[i-1]==2:
            diff[0]+=1
        elif arr[i]-arr[i-1]>3:
            print('NO')
            ch=False
            break
    if ch:
        if diff[1]<=1 and diff[0]==0:
            print('YES')
        elif diff[1]==0 and diff[0]<=2:
            print('YES')
        else:
            print('NO')
            
            t = int(input())
for Case in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    inds = {}
    for i in range(n):
        if a[i] not in inds:
            inds[a[i]] = []
        inds[a[i]].append(i)
    inds = sorted(inds.items(), key = lambda x: len(x[1]), reverse = True)
    res = [0]*n
    while inds:
        last = inds[-1][0]
        ind = inds[-1][1].pop()
        for i in range(len(inds)-1):
            res[ind] = inds[i][0]
            ind = inds[i][1].pop()
        res[ind] = last
        while inds and not inds[-1][1]:
            inds.pop()
    for num in res:
        print(num, end=" ")
    print()