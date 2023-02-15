# import sys
# input = sys.stdin.readline
def sol(arr):
    l = 0
    r = len(arr) - 1
    while l<len(arr) and not arr[l] : l += 1
    while r >= 0 and not arr[r] : r -= 1
    
    step = []
    cnt = 1
    total = 0
    for i in range(l+1, r+1):
        if arr[i] == 0:
            total += 1
        if arr[i] == arr[i-1]:
            cnt += 1
        else:
            step.append(cnt)
            cnt = 1
            
    step.append(cnt)
    if len(step) == 1:
        return 0
    
    best = total 
    left = [(0, 0)]
    cnt1 = 0
    cnt0 = 0
    
    for i in range(0, len(step)-1, 2):
        cnt1 += step[i]
        cnt0 += step[i+1]
        left.append((cnt1, cnt0))
        best = min(best, max(cnt1, total - cnt0))
        if cnt1 >= total - cnt0:
            break
        

    cnt1 = 0
    cnt0 = 0
    ind = len(left) - 1
    for i in range(len(step) - 1, 0, -2):
        cnt1 += step[i]
        cnt0 += step[i-1]
        best = min(best, max(cnt1, total - cnt0))
        while ind >= 0:
            a = cnt1 + left[ind][0]
            b = cnt0 + left[ind][1]
            best = min(best, max(a, total - b))
            if a <= total - b:
                ind += 1
                if ind == len(left):
                    ind -= 1
                break
            ind -= 1
    return best
        
        
    
t = int(input())
for case in range(t):
    arr = input()
    arr = [int(i) for i in arr]
    print(sol(arr))