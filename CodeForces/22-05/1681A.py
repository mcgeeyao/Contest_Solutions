import sys
input = sys.stdin.readline
def sol(n, a, m, b):
    ma = max(a)
    mb = max(b)
    if ma > mb:
        return 'Alice\nAlice'
    elif ma < mb:
        return 'Bob\nBob'
    else:
        return 'Alice\nBob'
    
 
t = int(input())
for case in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    print(sol(n, a, m, b))