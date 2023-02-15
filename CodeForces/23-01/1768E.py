import sys
input = sys.stdin.readline

t = 2 * (10 ** 6) + 5

n, mod = list(map(int,input().split()))
t = 2 * (n) + 5
frac = [1] * t
inv = [1] * t
curr = 1
for i in range(1, t):
    curr *= i
    curr %= mod
    frac[i] = curr
    
curr = 1
for i in range(1, t):
    curr *= pow(i, mod - 2, mod)
    curr %= mod
    inv[i] = curr
    
res = 0
res += frac[2 * n] * 2
res %= mod
res -= frac[n]
res -= 1
res %= mod



res += frac[2 * n] * (4 * (frac[2 * n] * inv[n] % mod - frac[n])) % mod



tmp = frac[2 * n]
tmp = (frac[2 * n] * tmp) % mod
tmp = (inv[n] * tmp) % mod
tmp1 = 0
for k in range(n + 1):
    tmp2 = frac[n]
    tmp2 = (frac[n] * tmp2) % mod
    tmp2 = (frac[n] * tmp2) % mod
    tmp2 = (inv[k] * tmp2) % mod
    tmp2 = (inv[n - k] * tmp2) % mod
    tmp2 = (inv[k] * tmp2) % mod
    tmp2 = (inv[n - k] * tmp2) % mod
    tmp2 = (frac[2*n - k] * tmp2) % mod
    tmp2 = (inv[n - k] * tmp2) % mod
    tmp1 = (tmp2 + tmp1) % mod
res += (tmp * 2 - tmp1) * 3 % mod
res %= mod
# res += (tmp - frac[n]) * 4
res -= 4 * ((frac[n] * frac[n]) % mod) * frac[n] % mod
print(tmp, tmp1)
res %= mod
print(res)