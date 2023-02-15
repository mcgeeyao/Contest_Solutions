
t=int(input())
for case in range(t):
    aabb=input()
    curr=1
    ch=True
    for i in range(1,len(aabb)):
        if aabb[i]==aabb[i-1]:
            curr+=1
        else:
            if curr==1:
                print('NO')
                ch=False
                break      
            else:
                curr=1
    if ch:
        if curr==1:
            print('NO')
        else:
            print('YES')
    