import sys
input = sys.stdin.readline
 
n, q = list(map(int,input().split()))
arr = list(map(int,input().split()))
querys = list(map(int,input().split()))
 
arr.sort()

lessThanN = [0] * n
lessThanN[0] = arr[0]
for i in range(1, n):
    lessThanN[i] = min(lessThanN[i-1] + 1, arr[i])
 
for k in querys:
    if k < n:
        print(lessThanN[k], end = ' ')
        continue
    if (k - n) & 1:
        tmp = [arr[i] + k - i for i in range(n-1)]+[arr[-1]]
        minus = (k-n+1) // 2
        mn = min(tmp)
        diff = 0
        for i in tmp:
            diff += i - mn
            
        if diff < minus:
            print(mn - (minus - diff)//n - ((minus - diff)%n > 0), end = ' ')
        else:
            print(mn, end = ' ')
    else:
        tmp = [arr[i] + k - i for i in range(n)]
        minus = (k-n) // 2
        mn = min(tmp)
        diff = 0
        for i in tmp:
            diff += i - mn
            
        if diff < minus:
            print(mn - (minus - diff)//n -  ((minus - diff)%n > 0), end = ' ')
        else:
            print(mn, end = ' ')
print()