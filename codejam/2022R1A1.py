t=int(input())
def sol(s):
    res=s[-1]
    pre=ord(s[-1])
    con=False
    for i in range(len(s)-2,-1,-1):
        if ord(s[i])<pre:
            res+=s[i]*2
            con=True
            pre=ord(s[i])
        elif ord(s[i])>pre:
            res+=s[i]
            con=False
            pre=ord(s[i])
        else:
            if con:
                res+=s[i]*2
            else:
                res+=s[i]
    return res[::-1]

for case in range(t):
    s=input()
    print(f'Case #{case+1}: {sol(s)}')