import sys
input = sys.stdin.readline
def sol(arr, n):
    pass
 
t = int(input())
for case in range(t):
    a = input()
    s = input()
    se = set()
    se.add(a[0])
    se.add(a[1])
    se.add(s[0])
    se.add(s[1])
    print(len(se) - 1)
