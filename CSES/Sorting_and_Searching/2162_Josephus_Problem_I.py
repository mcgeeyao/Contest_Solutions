import sys
input = sys.stdin.readline
def sol(n):
    if n == 1:
        print(1)
        return 
    right = [(i + 1) % n for i in range(n)]
    left = [(i - 1) % n for i in range(n)]
    curr = 1
    while right[curr] != curr:
        print(curr + 1, end=' ')
        right[left[curr]] = right[curr]
        left[right[curr]] = left[curr]
        curr = right[right[curr]]
    print(curr + 1)
    
    
n = int(input())
(sol(n))
