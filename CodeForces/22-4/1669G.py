t=int(input())

for case in range(t):
    m,n=list(map(int,input().split()))
    grid=[[0]*n for _ in range(m)]
    for i in range(m):
        tmp=input()
        for  j in range(n):
            if tmp[j]=='*':
                grid[i][j]=1
            elif tmp[j]=='o':
                grid[i][j]=2
    for j in range(n):
        cnt=0
        for i in range(m):
            if grid[i][j]==1:
                cnt+=1
                grid[i][j]=0
            elif grid[i][j]==2:
                for k in range(cnt):
                    grid[i-k-1][j]=1
                cnt=0
        for k in range(cnt):
            grid[-k-1][j]=1
    for i in range(m):
        for j in range(n):
            if grid[i][j]==0:
                print('.',end='')
            elif grid[i][j]==1:
                print('*',end='')
            else:
                print('o',end='')
        print()
        
                
        
    