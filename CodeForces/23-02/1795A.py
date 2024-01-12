import sys
input = sys.stdin.readline
def sol(s1, s2, m, n):
    i = 1
    for i in range(1, m):
        if s1[i] == s1[i-1]:
            break
        i += 1
    j = 1
    for j in range(1, n):
        if s2[j] == s2[j-1]:
            break
        j += 1
    if i != m and j != n: return 'NO'
    if i != m:
        s1 += s2[-1]
        for k in range(m-1, i-1, -1):
            if s1[k] == s1[k+1]:
                return 'NO'
    elif j != n:
        s2 += s1[-1]
        for k in range(n-1, j-1, -1):
            if s2[k] == s2[k+1]:
                return 'NO'
    return 'YES'
    
 
t = int(input())
for case in range(t):
    m, n = list(map(int, input().split()))
    s1 = input()[:-1]
    s2 = input()[:-1]
    print(sol(s1, s2, m, n))
