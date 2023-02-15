import sys
input = sys.stdin.readline
def sol(arr, n):
    pos = 0
    neg = 0
    tmp = []
    check = False
    for i in arr:
        if not check and i == 0: 
            tmp.append(0)
            check = True
        if i < 0: neg += 1
        if i > 0: pos += 1
        if i != 0: tmp.append(i)
    if neg >= 3 or pos >= 3:
        return 'NO'
    for i in range(len(tmp)-2):
        for j in range(i+1, len(tmp)-1):
            for k in range(j+1, len(tmp)):
                if tmp[i] + tmp[j] + tmp[k] not in tmp:
                    return "NO"
    return 'Yes'
    
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
