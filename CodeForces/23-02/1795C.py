import sys
input = sys.stdin.readline
def sol(n, a, b):
    b = b[::-1]
    a = a[::-1]
    pre = [0]
    res = [0] * n
    plus = [0] * (n + 1)
    for i in b:
        pre.append(pre[-1] + i)
    for i in range(n):
        l = 0
        r = i+1
        while l <= r:
            mid = (l + r) >> 1
            if pre[i+1] - pre[mid] <= a[i]:
                r = mid - 1
            else:
                l = mid + 1
        plus[i + 1] -= 1
        plus[l] += 1
        if l:
            res[l-1] += a[i] - (pre[i+1] - pre[l])
            
    pre2 = [0]
    for i in plus:
        pre2.append(pre2[-1] + i)

    for i in range(n):
        res[i] += b[i] * pre2[i+1]
        
    for i in res[::-1]:
        print(i, end=' ')
    print()
    
t = int(input())
for case in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    (sol(n, a, b))
