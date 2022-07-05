
t=int(input())
for case in range(t):
    n=int(input())
    arr=input()
    if n==1 and arr!='W':
        print('NO')
        continue
    s=''
    ch=True
    for i in arr:
        if i=='W':
            if s and ('B' not in s or 'R' not in s):
                print('NO')
                ch=False
                break
            s=''
        else:
            s+=i
    if ch:
        if s and ('B' not in s or 'R' not in s):
            print('NO')
            ch=False
        else:
            print('YES')
            
        
        
        
    
        
        
    