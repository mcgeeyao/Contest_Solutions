import sys
import math
input = sys.stdin.readline
def din(a, b, c):
    return (-b / (2 * a), (4 * a * c - b * b) / (4 * a))
def sol(straights, pus, n, m):
    z = 0 in straights
    s = sorted(straights)
    res = []
    for a, b, c in pus:
        x, y = din(a, b, c)
        if y > 0 and z: 
            res.append("YES \n0\n")
            continue
        if a * c < 0:
            res.append("NO")
            continue
        lower = b - 2 * math.sqrt(a * c)
        upper = b + 2 * math.sqrt(a * c)
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) >> 1
            if s[mid] > lower:
                r = mid - 1
            else:
                l = mid + 1
        l1 = l
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) >> 1
            if s[mid] >= upper:
                r = mid - 1
            else:
                l = mid + 1
        r1 = r
        if l1 <= r1:
            res.append(f"YES \n{s[l1]}\n")
        else:
            res.append("NO")
    for i in res:
        print(i)
        
 
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    straights = []
    for i in range(n):
        straights.append(int(input()))
    pus = []
    for i in range(m):
        pus.append(list(map(int,input().split())))
    (sol(straights, pus, n, m))
