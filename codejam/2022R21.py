import sys
input = sys.stdin.readline
t = int(input())
def sol(n, k):
    if k % 2 or k < n:
        return 'IMPOSSIBLE'
    
    turn = 0
    tmpk = k
    tmpn = n
    res = []
    base = 0
    while tmpn > 1:
        while tmpk - 2 <= (tmpn - 2) ^ 2 - 1:
            tmpk -= 2
            tmpn -= 2
            turn += 1
            res.append((base + 1, base + tmpn^2 - (tmpn-1)^2))
            base += tmpn^2 - (tmpn-1)^2         
        diff = tmpk - 2 - ((tmpn - 2) ^ 2 - 1)
        diff //= 2
        
    
    
        
        
        
    

for _ in range(t):
    n, k = list(map(int, input().split()))
    
    print(f'Case #{case+1}: {sol(n, k)}')