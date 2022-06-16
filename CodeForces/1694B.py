import sys
input = sys.stdin.readline
def sol(s, n):
    res = n
    last = 0
    for i in range(1, n):
        if s[i] ^ s[i - 1]:
            res += i
    return res
            
 
t = int(input())
for case in range(t):
    n = int(input())
    s = [int(i) for i in input()[:-1]]
    print(sol(s, n))
