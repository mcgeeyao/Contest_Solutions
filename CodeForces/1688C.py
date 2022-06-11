import sys
input = sys.stdin.readline
def sol(arr, n):
    cnt = [0] * 26
    one = set()
    for i in arr:
        if len(i) == 1:
            one.add(i)
        for j in i:
            cnt[ord(j) - ord('a')] += 1
    for i in one:
        if cnt[ord(i) - ord('a')] % 2:
            return i
            
        
    
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = []
    for _ in range(2*n + 1):
        arr.append(input()[:-1])
    print(sol(arr, n))
