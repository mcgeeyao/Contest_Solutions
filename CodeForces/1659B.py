t=int(input())
for case in range(t):
    n,k=list(map(int,input().split()))
    bits=input()
    flip=[0]*n
    if k==0:
        print(bits)
        print('0 '*n)
        continue
    if k%2:
        for i in range(n):
            if bits[i] =='1':
                k-=1
                flip[i]+=1
            if k==0:break
        if k and k%2==0:
            print('1'*n)
            flip[0]+=k
            for i in range(n):
                print(flip[i],end=' ')
            print()
        elif k and  k%2:
            print('1'*(n-1)+'0')
            flip[0]+=k-1
            flip[-1]+=1
            for i in range(n):
                print(flip[i],end=' ')
            print()
        else:
            for i in range(n):
                if flip[i]==0 and bits[i] =='1':
                    print('0',end='')
                else:
                    print('1',end='')
            print()
            for i in range(n):
                print(flip[i],end=' ')
            print()
    else:
        for i in range(n):
            if bits[i] =='0':
                k-=1
                flip[i]+=1
            if k==0:break
        if k and k%2==0:
            print('1'*n)
            flip[0]+=k
            for i in range(n):
                print(flip[i],end=' ')
            print()
        elif k and  k%2:
            print('1'*(n-1)+'0')
            flip[0]+=k-1
            flip[-1]+=1
            for i in range(n):
                print(flip[i],end=' ')
            print()
        else:
            for i in range(n):
                if flip[i]==1:
                    print('1',end='')
                else:
                    print(bits[i],end='')
            print()
            for i in range(n):
                print(flip[i],end=' ')
            print()