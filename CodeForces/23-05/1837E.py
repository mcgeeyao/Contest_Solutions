import sys
input = sys.stdin.readline
def sol(arr, k):
    d = dict()
    n = 1<<k
    for i in range(n):
        if arr[i] != -1:
            d[arr[i]-1] = i
    bt = [0] * (2*n-1)
    for i in range(n-1, 2*n-1):
        bt[i] = 1 if arr[i-n+1] == -1 else 0
    res = 1
    mod = 998244353
    for i in range(k-1, 0, -1):
        # [2**i + 1: 2**(i+1)]
        h = set()
        cnt = 0
        for j in range((1<<i), (1<<(i+1))):
            bt[j-1] = bt[(j-1)*2+1] + bt[(j-1)*2+2]
            if j in d:
                if d[j] // (1 << (k-i)) + (1<<i) - 1 in h:
                    return 0
                h.add(d[j] // (1 << (k-i)) + (1<<i) - 1)
            else:
                cnt += 1
                res *= cnt
                res %= mod
        for j in range((1<<i), (1<<(i+1))):
            if j-1 not in h:
                res *= bt[j-1]
                res %= mod
                bt[j-1] -= 1

    if 0 in d or 1 in d:
        return res % mod
    else:
        return (2 * res) % mod
    
    return res

k = int(input())
arr = list(map(int,input().split()))
print(sol(arr, k))
