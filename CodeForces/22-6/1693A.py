import sys
input = sys.stdin.readline
def sol(arr, n):
    r = n - 1
    while r >= 0 and not arr[r]:
        r -=1 
    if r < 0: return 'YES'
    if arr[0] < 0: return 'NO'
    if sum(arr) != 0: return 'NO'
    if arr[r] > 0: return 'NO'
    tmp = -arr[r]
    for i in range(r - 1, 0, -1):
        if arr[i] >= tmp:
            return 'NO'
        tmp -= arr[i]
    return 'YES' 
        
        
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
