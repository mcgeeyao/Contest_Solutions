
t=int(input())
for case in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ch=True
    for i in range(n):
        if i%2:
            if arr[i]%2 != arr[1]%2:
                print('NO')
                ch=False
                break
        else:
            if arr[i]%2 != arr[0]%2:
                print('NO')
                ch=False
                break
    if ch:
        print('YES')