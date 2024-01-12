import sys
input = sys.stdin.readline
mod = 998244353


n, a1, x, y, m, k = list(map(int,input().split()))
s = input()
fac = [1] * (n+1)
inv = [1] * (n+1)
for i in range(2, n):
    fac[i] = (fac[i-1] * i) % mod
    inv[i] = (inv[i-1] * pow(i, mod-2, mod)) % mod
    
a = 
res = a1 if k == 1 else 0
for i in range(n-k+1):
    
    

