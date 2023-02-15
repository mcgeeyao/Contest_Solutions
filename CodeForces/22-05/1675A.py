
def sol(a, b, c, x, y):
    if a >= x :
        x = 0
    else:
        x -= a
    if b >= y :
        y = 0
    else:
        y -= b
    if c >= x + y:
        return 'YES'
    else:
        return 'NO'
    
t=int(input())
for case in range(t):
    a, b, c, x, y = list(map(int,input().split()))
    print(sol(a, b, c, x, y))