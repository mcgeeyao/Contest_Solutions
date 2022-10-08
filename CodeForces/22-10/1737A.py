import sys
input = sys.stdin.readline
def mp(a):
    return ord(a) - 97
def sol(s, n, m):
    cnt = [0] * 26
    for i in s:
        cnt[mp(i)] += 1
    d = n // m
    res = ''
    for i in range(m):
        tmp = 1
        for j in range(d):
            if not cnt[j]:
                tmp = 0
                break
            else:
                cnt[j] -= 1
                
        res += chr(97 + j + tmp)
    return res
        
 
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    s = input()[:-1]
    print(sol(s, n, m))
