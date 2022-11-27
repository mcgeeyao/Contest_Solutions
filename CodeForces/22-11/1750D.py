import sys
input = sys.stdin.readline
def sol(arr, n, m):
    res = 1
    for i in range(1, n):
        if arr[i] > arr[i - 1]: return 0
        if arr[i] == arr[i - 1]:
            res *= m // arr[i]
        elif arr[i - 1] % arr[i] != 0: return 0
        else:           
            res *= m // arr[i] - m // (arr[i - 1])
        res %= 998244353
    return res

a = 1000000000
res = 1
res *= (a // 30 + 1) // 2
res %= 998244353
res *= ((a + 1) * 2 * 4) // 30
res %= 998244353
res *= a
res %= 998244353
print(res)

t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(sol(arr, n, m))

