import sys
input = sys.stdin.readline
def sol(arr):
    if len(arr) <= 2:
        return arr[0]
    else:
        return min(arr)
    
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = []
    while n:
        arr.append(n % 10)
        n //= 10
    print(sol(arr))