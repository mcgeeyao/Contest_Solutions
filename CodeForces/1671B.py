
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