import sys
input = sys.stdin.readline
def sol(l1, r1, l2, r2):
    if r1 < l2 or r2 < l1:
        return l1 + l2
    return max(l1, l2)
     
t = int(input())
for case in range(t):
    l1, r1, l2, r2 = list(map(int,input().split()))
    print(sol(l1, r1, l2, r2))