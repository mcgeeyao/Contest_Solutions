t=int(input())
for case in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=0
    l=[0,0,0]
    one=0
    m=max(a)
    for num in a:
        i=m-num
        l[i%3]+=1
        res+=(i//3)
        one+=((i//3)+(i%3==1))//2

    if l[1]>l[2]:
        rem=(l[1]-l[2])
        rem1=rem%3
        rem2=rem//3
        if rem1==0:
            if one>=rem2:
                ans1=(res*2+l[2]*2+(rem2)*2)
            else:
                ans1=(res*2+l[2]*2+(one)*2+2*(rem-one*3)-1)
        elif rem1==1:
            if one>=rem2:
                ans1=(res*2+l[2]*2+(rem2)*2+1)
            else:
                ans1=(res*2+l[2]*2+(one)*2+2*(rem-one*3)-1)
        else:
            if one>rem2:
                ans1=(res*2+l[2]*2+(rem2)*2+2)
            elif one==rem2:
                ans1=(res*2+l[2]*2+(rem2)*2+3)
            else:
                ans1=(res*2+l[2]*2+(one)*2+2*(rem-one*3)-1)
    elif l[1]<l[2]:
        if (l[2]-l[1])%2==0:
            tmp1=((l[2]-l[1])//2)*3
        elif (l[2]-l[1])==1:
            tmp1=2
        else:
            tmp1=((l[2]-1-l[1])//2)*3+1
        ans1=(res*2+l[1]*2+tmp1)
    else:
        ans1=(res*2+l[1]*2)
        
        
        
    res=0
    l=[0,0,0]
    m=m+1
    one=0
    for num in a:
        i=m-num
        l[i%3]+=1
        res+=(i//3)
        one+=((i//3)+(i%3==1))//2
    if l[1]>l[2]:
        rem=(l[1]-l[2])
        rem1=rem%3
        rem2=rem//3
        if rem1==0:
            if one>=rem2:
                ans2=(res*2+l[2]*2+(rem2)*2)
            else:
                ans2=(res*2+l[2]*2+(one)*2+2*(rem-one*3)-1)
        elif rem1==1:
            if one>=rem2:
                ans2=(res*2+l[2]*2+(rem2)*2+1)
            else:
                ans2=(res*2+l[2]*2+(one)*2+2*(rem-one*3)-1)
        else:
            if one>rem2:
                ans2=(res*2+l[2]*2+(rem2)*2+2)
            elif one==rem2:
                ans2=(res*2+l[2]*2+(rem2)*2+3)
            else:
                ans2=(res*2+l[2]*2+(one)*2+2*(rem-one*3)-1)
    elif l[1]<l[2]:
        if (l[2]-l[1])%2==0:
            tmp1=((l[2]-l[1])//2)*3
        elif (l[2]-l[1])==1:
            tmp1=2
        else:
            tmp1=((l[2]-1-l[1])//2)*3+1
        ans2=(res*2+l[1]*2+tmp1)
    else:
        ans2=(res*2+l[1]*2)
        
        
    res=0
    l=[0,0,0]
    m=m+1
    one=0
    for num in a:
        i=m-num
        l[i%3]+=1
        res+=(i//3)
        one+=((i//3)+(i%3==1))//2
    if l[1]>l[2]:
        rem=(l[1]-l[2])
        rem1=rem%3
        rem2=rem//3
        if rem1==0:
            if one>=rem2:
                ans3=(res*2+l[2]*2+(rem2)*2)
            else:
                ans3=(res*2+l[2]*2+(one)*2+2*(rem-one*3)-1)
        elif rem1==1:
            if one>=rem2:
                ans3=(res*2+l[2]*2+(rem2)*2+1)
            else:
                ans3=(res*2+l[2]*2+(one)*2+2*(rem-one*3)-1)
        else:
            if one>rem2:
                ans3=(res*2+l[2]*2+(rem2)*2+2)
            elif one==rem2:
                ans3=(res*2+l[2]*2+(rem2)*2+3)
            else:
                ans3=(res*2+l[2]*2+(one)*2+2*(rem-one*3)-1)
    elif l[1]<l[2]:
        if (l[2]-l[1])%2==0:
            tmp1=((l[2]-l[1])//2)*3
        elif (l[2]-l[1])==1:
            tmp1=2
        else:
            tmp1=((l[2]-1-l[1])//2)*3+1
        ans3=(res*2+l[1]*2+tmp1)
    else:
        ans3=(res*2+l[1]*2)
        
    print(min(ans1,ans2,ans3))
    