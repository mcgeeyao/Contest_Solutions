import sys
input = sys.stdin.readline
def sol(arr, n):
    dp = [[10 ** 9] * n for _ in range(4)]
    d1 = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    d2 = 'ACGT'
    for i in range(4):
        dp[i][0] = 1
        if arr[0] == d2[i]: dp[i][0] += 1
    bt1 = [[10 ** 9] * n for _ in range(4)]
    bt2 = [[10 ** 9] * n for _ in range(4)]
    arr = [d1[i] for i in arr]
    for i in range(1, n):
        for j in range(4):
            for k in range(4):
                if dp[k][i-1] + (k != j) + (j == k == arr[i]) < dp[j][i]:
                    bt1[j][i] = k
                    bt2[j][i] = (k != j) + (j == k == arr[i])
                dp[j][i] = min(dp[j][i], dp[k][i-1] + (k != j) + (j == k == arr[i]))
    mn = min(dp[i][-1] for i in range(4))
    for i in range(4):
        if dp[i][-1] == mn:
            curr = i
    res = ''
    ind = n - 1
    while ind >= 0:
        if bt2[curr][ind]:   
            res += d2[curr]
        curr = bt1[curr][ind]
        ind -= 1
    # for i in range(4):
        
    #     print(dp[i])
    return (res[::-1])

s = input()[:-1]
print(sol(s, len(s)))
