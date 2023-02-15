import sys
input = sys.stdin.readline
def sol(n, s):
    st = set()
    for i in range(1, n - 1):
        if s[i: i + 2] in st:
            return 'YES'
        st.add(s[i - 1: i + 1])
    return 'NO'
 
t = int(input())
for case in range(t):
    n = int(input())
    s = input()
    print(sol(n, s))
