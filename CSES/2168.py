# 2169. Nested Ranges Count
# TLE for pypy
    
def sol(arr, n):
    sortx = sorted([(arr[ind][0], ind) for ind in range(n)], key=lambda x: (arr[x[1]][0], -arr[x[1]][1]))
    sorty = sorted([(arr[ind][1], ind) for ind in range(n)])
    d = {}
    for i in range(n):
        d[sorty[i][1]] = i
    seen = [0] * n
    mex = 0
    mx = -1
    
    res1 = [0] * n
    res2 = [0] * n
    for i in range(n):
        yi = arr[sortx[i][1]][1]
        idx = sortx[i][1]
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) >> 1
            if sorty[mid][0] <= yi:
                l = mid + 1
            else:
                r = mid - 1
        seen[d[idx]] = 1
        while (mex < n and seen[mex]): mex += 1
        res1[idx] = (mex <= r) * 1
        
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) >> 1
            if sorty[mid][0] < yi:
                l = mid + 1
            else:
                r = mid - 1
        res2[idx] = (mx >= l) * 1
        mx = max(mx, d[idx])
        
    for i in res1:
        print(i, end=' ')
    print()
    for i in res2:
        print(i, end=' ')
    # print(res1)
    # print(res2)
                
        
    
    
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
(sol(arr, n))
