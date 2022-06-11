import sys
input = sys.stdin.readline
def sol(arr, n):
    e_cnt = 0
    o_check = False
    min_bit = 1 << 100
    for i in arr:
        if i % 2 == 0:
            e_cnt += 1
            min_bit = min(min_bit, i&-i)
        else:
            o_check = True
    if o_check:
        return e_cnt
    else:
        cnt = 0
        while min_bit > 1:
            cnt += 1
            min_bit >>= 1
        return cnt + e_cnt - 1
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
