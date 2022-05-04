
def sol(x, y):
    if y % x or y == 0:
        return '0 0'
    else:
        return f'1 {y // x} '
    
    
    
t=int(input())
for case in range(t):
    x, y = list(map(int,input().split()))
    print(sol(x, y))