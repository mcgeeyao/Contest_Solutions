import sys
input = sys.stdin.readline
def sol(s):
    l = 0
    r = len(s) - 1
    while l < r and s[l] == s[r]:
        l += 1
        r -= 1
    
    for i in range(l, r + 1, 2):
        if s[i] != s[i+1]: return 'Alice'
    
    return 'Draw'
 
t = int(input())
for case in range(t):
    s = input()
    print(sol(s[:-1]))
