import sys
input = sys.stdin.readline
def sol(arr, n):
    o = 0
    z = 0
    res = 0
    curr = 0
    pre = 'a'
    for i in s:
        if i == pre:
            curr += 1
        else:
            res = max(res, curr)
            curr = 1
            pre = i
        if i == '0': z += 1
        else: o += 1
    res = max(res, curr)
    return max(res * res, o * z)
        
t = int(input())
for case in range(t):
    n = int(input())
    s = input()[:-1]
    print(sol(s, n))
