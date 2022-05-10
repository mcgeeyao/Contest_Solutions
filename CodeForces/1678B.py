import sys
input = sys.stdin.readline
def sol(s, n):
    
    
    arr = []
    curr = 1
    for i in range(1, n):
        if s[i] == s[i-1]:
            curr += 1
        else:
            arr.append(curr)
            curr = 1
    arr.append(curr)
    res = 0
    state = False
    curr = 0
    for i in arr:
        if state :
            if i%2:
                res += curr
                curr = 0
                state = False
            else:
                curr += 1
        else:
            if i%2:
                curr = 1
                state = True
    return res
t = int(input())
for case in range(t):
    n = int(input())
    arr = input()
    print(sol(arr, n))