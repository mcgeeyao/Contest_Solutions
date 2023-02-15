import sys
input = sys.stdin.readline
def sol(a, b, n):
    res1 = []
    for i in range(n):
        l = 0
        r = n-1
        while l <= r:
            mid = (l + r) >> 1
            if b[mid] >= a[i]:
                r = mid - 1
            else:
                l = mid + 1
        res1.append(b[l] - a[i])
    last = n - 1
    res2 = []
    for i in range(n - 1, -1, -1):
        l = 0
        r = last
        while l <= r:
            mid = (l + r) >> 1
            if b[mid] >= a[i]:
                r = mid - 1
            else:
                l = mid + 1
        res2.append(b[last] - a[i])
        if l == i: 
            last = i - 1
    res2 = res2[::-1]
    for i in range(n):
        print(res1[i], end=' ')
    print()
    for i in range(n):
        print(res2[i], end=' ')
    
                
 
t = int(input())
for case in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    (sol(a, b, n))
