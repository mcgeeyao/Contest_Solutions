import sys
input = sys.stdin.readline
def sol(n):
    a = 1
    b = 2
    for i in range(3, n + 1):
        print(f'? {a} {i}')
        sys.stdout.flush()
        tmp1 = int(input())
        print(f'? {b} {i}')
        sys.stdout.flush()
        tmp2 = int(input())
        if tmp1 == tmp2:
            continue
        elif tmp1 > tmp2:
            b = i
        else:
            a = i
    print(f'! {a} {b}')
    sys.stdout.flush()
    return int(input())
 
t = int(input())
for case in range(t):
    n = int(input())
    if sol(n) == -1: break
