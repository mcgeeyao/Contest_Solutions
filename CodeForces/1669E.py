
t=int(input())
for case in range(t):
    n=int(input())
    mp1=[[0]*26 for i in range(26)]
    mp2=[[0]*26 for i in range(26)]
    for i in  range(n):
        s=input()
        a=ord(s[0])-ord('a')
        b=ord(s[1])-ord('a')
        mp1[a][b]+=1
        mp2[b][a]+=1
    res=0
    for i in range(26):
        
        tmp=sum(mp1[i])
        su=(tmp*(tmp-1))//2
        for j in range(26):
            if mp1[i][j]>1:
                
                su-=((mp1[i][j])*(mp1[i][j]-1))//2
        
        res+=su
        
        tmp=sum(mp2[i])
        su=(tmp*(tmp-1))//2
        for j in range(26):
            if mp2[i][j]>1:
                su-=((mp2[i][j])*(mp2[i][j]-1))//2
        res+=su
    print(res)
        
        
    
        
        
    