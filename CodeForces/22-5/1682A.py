import sys
input = sys.stdin.readline
def sol(n, s):

    if n%2:
        res = 1
        l = n // 2
        while l >= 0 and s[l] == s[l-1]:
            l -= 1
            res += 1
        r = n // 2 
        while r < n and s[r] == s[r+1]:
            r += 1
            res += 1
        return res
    else:
        res = 2
        l = n // 2 - 1
        while l >= 0 and s[l] == s[l-1]:
            l -= 1
            res += 1
        r = n // 2 
        while r < n and s[r] == s[r+1]:
            r += 1
            res += 1
        return res
        
    

t = int(input())
for case in range(t):
    n = int(input())
    arr = input()
    print(sol(n, arr))