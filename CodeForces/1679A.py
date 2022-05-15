import sys
input = sys.stdin.readline
def sol(n):
    if n < 4 or n % 2:
        return '-1'
    Min = n // 6  + ((n % 6) > 0)
    Max = n//4
    return str(Min) + ' ' + str(Max)
    
    
    
    return 
     
t = int(input())
for case in range(t):
    n = int(input())
    print(sol(n))