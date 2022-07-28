import sys
input = sys.stdin.readline
def sol(arr, n, m, k):
    arr = sorted(arr, reverse=True)
    cnt = n
    re = 0
    for i in arr:
        tmp = i // m
        if tmp < 2:
            break
        if (cnt - tmp) % 2 and tmp == 2:
            break
        if (cnt - tmp) % 2:
            cnt -= tmp - 1
            re += 1
        else:
            cnt -= tmp
        if cnt - re <= 0: return 'YES'
            
    cnt = m
    re = 0
    for i in arr:
        tmp = i // n
        if tmp < 2:
            break
        if (cnt - tmp) % 2 and tmp == 2:
            break
        if (cnt - tmp) % 2:
            cnt -= tmp - 1
            re += 1
        else:
            cnt -= tmp
        if cnt - re <= 0: return 'YES'
        
    return 'NO'
     
t = int(input())
for case in range(t):
    n, m, k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(sol(arr, n, m, k))
