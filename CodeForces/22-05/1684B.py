import sys
input = sys.stdin.readline
def sol(arr):
    return str(sum(arr)) + ' ' + str(arr[1] + arr[2]) + ' ' + str(arr[2])
    
    
 
t = int(input())
for case in range(t):
    arr = list(map(int,input().split()))
    print(sol(arr))