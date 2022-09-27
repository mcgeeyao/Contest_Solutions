import sys
input = sys.stdin.readline
def sol(a, b, n):
    al = [0] * 26
    a = a[::-1]
    indsa = [list() for i in range(26)]
    indsb = [list() for i in range(26)]
    for i in range(n):
        al[ord(a[i]) - ord('a')] += 1
        al[ord(b[i]) - ord('a')] += 1
        indsa[ord(a[i]) - ord('a')].append(i)
        indsb[ord(b[i]) - ord('a')].append(i)
    for i in range(26):
        if al[i] & 1: return 'NO'
    cnt = 0
    for i in range(26):
        if len(indsa[i]) == len(indsb[i])  and len(indsb[i]) & 1:
            if indsb[i][0] == indsa[i][0]:
                cnt += 1
    if n & 1:
        if cnt >= 2: return 'NO'
    else:
        if cnt: return 'NO'
    return 'YES'
    

t = int(input())
for case in range(t):
    n = int(input())
    a = input()[:-1]
    b = input()[:-1]
    print(sol(a, b, n))
