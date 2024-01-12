import sys
input = sys.stdin.readline
def sol(arr, n):
    state = 0
    res = 1
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            if state != 1:
                res += 1
            state = 1
        elif arr[i] < arr[i-1]:
            if state != -1:
                res += 1
            state = -1
        # else:
        #     if state != -1:
        #         res += 1
        #     state = -1
    return res
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
