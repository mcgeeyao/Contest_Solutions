import sys
input = sys.stdin.readline

def sol(arr, n, k):
    arr = sorted(arr)
    c = {}
    if k >= n:
        return (0)
    for num in arr:
        if num not in c:
            c[num] = 0
        c[num] += 1
    arr = sorted(c.items())
    
    diff = [0]*len(arr)
    pre = 0
    for i in range(len(arr)):
        diff[i] = arr[i][0] - pre
        pre = arr[i][0]+1
        
    end = None
    MEX = 0
    for i in range(len(diff)):
        if diff[i] <= k:
            k -= diff[i]
            MEX = arr[i][0]
        else:
            end = sorted(arr[i:], key = lambda x: x[1], reverse=True)
            break
    if not end:
        return (0)
    else:
        while k >= end[-1][1]:
            k -= end.pop()[1]
        return (len(end))    
    
        
            
            
t = int(input())
for case in range(t):
    n, k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(sol(arr, n, k))