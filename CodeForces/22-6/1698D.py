import sys
input = sys.stdin.readline
def sol(n):
    l = 1
    r = n
    while l < r:
        mid = (l + r) // 2
        print('?', l, mid, flush=True)
        arr = list(map(int, input().split()))
        cnt = 0
        for i in arr:
            if l <= i <= mid:
                cnt += 1
            if i > mid: break
        if cnt & 1:
            r = mid
        else:
            l = mid + 1
    return l
        
    
 
t = int(input())
for case in range(t):
    n = int(input())
    print('!', sol(n), flush=True)
