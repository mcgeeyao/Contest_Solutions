import sys
input = sys.stdin.readline
def sol(s):
    return s + s[::-1]
 
t = int(input())
for case in range(t):
    s = input()[:-1]
    print(sol(s))
