
import sys
input = sys.stdin.readline
def sol(arr, n, s):
    last = 0
    res = 0
    for i in range(n):
        if arr[ord(s[i]) - ord('a')]:
            res = max(res, i - last)
            last = i
            
    return res
        
    
t = int(input())
for case in range(t):
    n = int(input())
    s = input()
    S = list(input().split())
    arr = [0] * 26
    for i in S[1:]:
        arr[ord(i) - ord('a')] += 1
    print(sol(arr, n, s))