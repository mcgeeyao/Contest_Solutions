import sys
input = sys.stdin.readline
def sol(n, a, b):
    ra = ''
    for i in a:
        if i == '0': ra += '1'
        if i == '1': ra += '0'
    if a == b or ra == b:
        res = []
        state = int(b[0])
        for i in range(n):
            if a[i] == '0':
                res.append([i, i])
                if i > 0:
                    state ^= 1
        if state:
            res.append([0, 0])
            res.append([1, n - 1])
        else:
            res.append([0, n - 1])
                
                
        print('YES')
        print(len(res))
        for i, j in res:
            print(i + 1, j + 1)
            
    else:
        print('NO')
        
 
t = int(input())
for case in range(t):
    n = int(input())
    a = input()[:-1]
    b = input()[:-1]
    (sol(n, a, b))
