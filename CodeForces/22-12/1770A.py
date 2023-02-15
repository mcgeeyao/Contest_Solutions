import sys
import heapq
input = sys.stdin.readline
def sol(n, m, a, b):
    a = sorted(a)
    heapq.heapify(a)
    for i in b:
        heapq.heappop(a)
        heapq.heappush(a, i)
    return sum(a)
            
 
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(sol(n, m, a, b))
