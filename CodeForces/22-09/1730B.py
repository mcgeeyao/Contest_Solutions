import sys
input = sys.stdin.readline
def sol(arr, arr2, n):
    a = [(arr[i] - arr2[i]) for i in range(n)]
    b = [(arr[i] + arr2[i]) for i in range(n)]
    return (min(a) + max(b)) / 2
    
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    print(sol(arr, arr2, n))
