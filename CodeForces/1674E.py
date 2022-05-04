
import math

def between(x, y):
    if x < y:
        x, y = y, x
    if x >= y*2:
        return (x+1)//2
    else:
        tmp = math.ceil((2*y-x)/3)
        x -= tmp
        return (x+1)//2+tmp
    
def sol(arr, n):
    #case 1 two min
    res = 10**18
    mi = 10**18
    secmi = 10**18
    for i in arr:
        if i < mi:
            secmi = mi
            mi = i
        elif i < secmi:
            secmi = i
    res = math.ceil(secmi/2) + math.ceil(mi/2)
    
    for i in range(2, n):
        res = min(res, min(arr[i], arr[i-2]) + math.ceil((max(arr[i], arr[i-2]) - min(arr[i], arr[i-2]))/2))
    
    for i in range(1, n):
        res = min(res, between(arr[i], arr[i-1]))
    return res
    
n = int(input())
arr = list(map(int,input().split()))
print(sol(arr, n))