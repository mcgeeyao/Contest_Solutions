t=int(input())
for case in range(t):
    n=int(input())
    c=list(map(int,input().split()))
    accu=0
    curr=0
    a=[-1]*n
    for  i in range(n):
        j=0
        while j<(c[i]-accu):
            if (curr==n):
                break
            a[curr]=1
            c[curr]-=curr
            curr+=1
            j+=1
        if (curr<n):
            a[curr]=0
            curr+=1
        else:
            break
        
        accu = c[i]
    for i in range(len(a)):
        print(a[i],end=' ')
    print()
   