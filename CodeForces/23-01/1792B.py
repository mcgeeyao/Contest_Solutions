import sys
input = sys.stdin.readline
def sol(a1, a2, a3, a4):
    if a1 == 0: return 1
    a = a1
    b = a1
    diff = abs(a2 - a3)
    if diff > a1:
        return min(a2, a3) * 2 + a1 + 1 + a1
    return a1 + a2 + a3 + min(a4, a1 - diff + 1)
    
    

 
t = int(input())
for case in range(t):
    a1, a2, a3, a4 = list(map(int,input().split()))
    print(sol(a1, a2, a3, a4))
