import sys
input = sys.stdin.readline
def sol(a, b):
    if a[0] == b[0]:
        return 'YES\n' + a[0] + '*'
    if a[-1] == b[-1]:
        return 'YES\n' + '*' + a[-1]
    s = set()
    for i in range(len(a)-1):
        s.add(a[i:i+2])
    for i in range(len(b)-1):
        if (b[i:i+2]) in s:
            return 'YES\n' + '*' + b[i:i+2] + '*'
    return 'NO'
    
t = int(input())
for case in range(t):
    a = input()[:-1]
    b = input()[:-1]
    print(sol(a, b))
