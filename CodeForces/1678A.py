import sys
input = sys.stdin.readline
def sol(arr, n):
    z = False
    non = 0
    same = False
    s = set()
    for i in arr:
        if i :
            non += 1
            if i in s:
                same = True
            s.add(i)
        else:
            z = True
    if z :
        return non
    if same:
        return non
    return non + 1
    
    
            
    
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))