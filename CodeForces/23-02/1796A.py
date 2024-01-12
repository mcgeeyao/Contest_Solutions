import sys
input = sys.stdin.readline
st = set()
a = 'FFBFFBFB' * 3
for i in range(1, 11):
    for j in range(len(a) - i):
        st.add(a[j:j+i])
def sol(s, n):
    if s in st: return 'YES'
    else: return 'NO'
t = int(input())
for case in range(t):
    n = int(input())
    s = input()[:-1]
    print(sol(s, n))
