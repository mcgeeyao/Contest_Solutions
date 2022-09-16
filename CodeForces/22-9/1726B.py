import sys
input = sys.stdin.readline
def sol(n, m):
    if n > m:
        print("NO")
    else:
        if n % 2:
            a = [1] * (n - 1)
            print("YES")
            print(*a, m - n + 1)
        else:
            if (m - n + 2) % 2 == 0:
                a = [1] * (n - 2)
                print("YES")
                print(*a, (m - n + 2)//2, (m - n + 2)//2)
            else:
                print('NO')
            
 
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    (sol(n, m))
