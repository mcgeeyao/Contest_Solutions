from heapq import heappop, heappush
import sys
input = sys.stdin.readline
def sol(arr, n, k):
    r = n - 1
    while r >= 0 and arr[r] == 0:
        r -= 1
    l = 0
    while l < n and arr[l] == 0:
        l += 1  
    if l != r :
        if r >= 0:
            if k >= l + n - 1 - r :
                arr[l] = 0
                arr[r] = 0
                arr[0] = 1
                arr[-1] = 1
            elif k >= n - 1 - r :
                arr[r] = 0
                arr[-1] = 1
            elif k >= l:
                arr[l] = 0
                arr[0] = 1
    else:
        if k >= n - 1 - r:
            arr[r] = 0
            arr[-1] = 1
        elif k >= l:
            arr[l] = 0
            arr[0] = 1
    res2 = 0
    for i in range(n-1):
        res2 += arr[i] * 10
        res2 += arr[i + 1]
    return res2
    
# def sol(arr, n, k):
#     arr2 = list(arr)
    
#     before = [0] * n
#     after = [0] * n
#     cnt = 0
#     for i in range(n):
#         before[i] = cnt
#         if arr[i]: cnt += 1
        
#     cnt = 0
#     for i in range(n - 1, -1, -1):
#         before[i] = cnt
#         if arr[i]: cnt += 1
        
#     r = n - 1
#     while r >= 0 and arr[r] == 0:
#         r -= 1
#     if r > 0:
#         arr1 = list(arr)
#         arr1[r] = 0
#         arr1[-1] = 1
        
#         heap = []
         
#         for i in range(n):
#             if arr[i]:
#                 if i - before[i] < n - 1 - i - after[i]:
#                     heappush(heap, (i, i, 1))
#                 else:
#                     heappush(heap, (n - 1 - i, i, 0))
                    
#         find = 0
#         eind = n - 1
#         while k:
#             v, ind, flag = heappop(heap)
#             if k >= v:
#                 k -= v
#                 if flag:
#                     arr2[ind] = 0
#                     arr2[find] = 1
#                     find += 1
#                 else:
#                     arr2[ind] = 0
#                     arr2[eind] = 1
#                     eind -= 1
#         res2 = 0
#         for i in range(n-1):
#             res2 += arr2[i] * 10
#             res2 += arr2[i + 1]
        
#     heap = []
         
#     for i in range(n):
#         if arr[i]:
#             if i - before[i] < n - 1 - i - after[i]:
#                 heappush(heap, (i, i, 1))
#             else:
#                 heappush(heap, (n - 1 - i, i, 0))
                
#     find = 0
#     eind = n - 1
#     while k:
#         v, ind, flag = heappop(heap)
#         if k >= v:
#             k -= v
#             if flag:
#                 arr2[ind] = 0
#                 arr2[find] = 1
#                 find += 1
#             else:
#                 arr2[ind] = 0
#                 arr2[eind] = 1
#                 eind -= 1
#     res = 0
#     for i in range(n-1):
#         res += arr2[i] * 10
#         res += arr2[i + 1]
#     return res
            
            

t = int(input())
for case in range(t):
    n, k = list(map(int,input().split()))
    tmp = input()
    arr = [int(i) for i in tmp[:-1]]
    print(sol(arr, n, k))
