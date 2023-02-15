import sys
input = sys.stdin.readline
     

n, q = list(map(int,input().split()))
arr = list(map(int,input().split()))
ch = set([i for i in range(n)])
s = sum(arr)
al = 0
for _ in range(q) :
    qu = list(map(int,input().split()))
    if qu[0] == 1:
        if qu[1] - 1 in ch:
            s += qu[2] - arr[qu[1] - 1]
            arr[qu[1] - 1] = qu[2]
            print(s)
        else :
            ch.add(qu[1] - 1)
            s += qu[2] - al
            arr[qu[1] - 1] = qu[2]
            print(s)
    else :
        ch = set()
        s = qu[1] * n
        al = qu[1]
        print(s)
        