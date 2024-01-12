import sys
input = sys.stdin.readline

n, q = list(map(int,input().split()))
arr = list(map(int,input().split()))
querys = list(map(int,input().split()))

arr.sort()

tmp1 = [arr[i] - i for i in range(n)]
mn1 = min(tmp1)
diff1 = 0
for i in tmp1:
    diff1 += i - mn1
    
tmp0 = [arr[i] - i for i in range(n-1)]
if n > 1:
    mn0 = min(tmp0)
else:
    mn0 = 0
diff0 = 0
for i in tmp0:
    diff0 += i - mn0

lessThanN = [0] * n
lessThanN[0] = arr[0]
for i in range(1, n):
    lessThanN[i] = min(lessThanN[i-1] + 1, arr[i])
    
for k in querys:
    if k < n:
        print(lessThanN[k], end = ' ')
        continue
    
    elif (k - n) & 1:
        if n == 1:
            print(arr[0] - (k) // 2, end = ' ')
            continue
        
        minus = (k-n+1) // 2
        if mn0 + k >= arr[-1]:
            diff = diff0 + (mn0 + k - arr[-1]) * (n-1)
            mn = arr[-1]
        else:
            diff = diff0 + (arr[-1] - mn0 - k)
            mn = mn0 + k
            
        if diff < minus and minus > 0:
            print(mn - (minus - diff)//n - ((minus - diff)%n > 0), end = ' ')
        else:
            print(mn, end = ' ')
    else:
        minus = (k-n) // 2
        if diff1 < minus and minus > 0:
            print(mn1 + k - (minus - diff1)//n -  ((minus - diff1)%n > 0), end = ' ')
        else:
            print(mn1 + k, end = ' ')
print()