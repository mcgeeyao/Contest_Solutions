import sys
input = sys.stdin.readline
def sol(n, s):
    cnt = 0
    mark = set()
    check = 0
    for i in range(n):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            check = 1
        if check:
            mark.add(i)
            if cnt == 0:
                check = 0
    if cnt != 0:
        print(-1)
        return 
    
    a = len(mark)
    if a == n or a == 0:
        print(1)
        for i in range(n):
            print(1, end=' ')
    else:
        print(2)
        for i in range(n):
            if i in mark: print(1, end=' ')
            else: print(2, end=' ')
    print()
 
t = int(input())
for case in range(t):
    n = int(input())
    s = input()[:-1]
    (sol(n, s))

