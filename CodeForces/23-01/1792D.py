import sys
input = sys.stdin.readline
def sol(arr, n, m):
    trie = [dict() for _ in range(11)]
    for i in range(n):
        st = sorted([(arr[i][j], j) for j in range(m)])
        curr = trie
        for j in range(m):
            if st[j][1] not in curr[j]:
                curr[j][st[j][1]] = [dict() for _ in range(11)]
            curr = curr[j][st[j][1]]
        
    res = [0] * n
    for i in range(n):
        curr = trie
        for j in range(m):
            if arr[i][j] - 1 not in curr[j]:
                break
            curr = curr[j][arr[i][j] - 1]
            res[i] = j + 1
    for i in res:
        print(i, end=' ')
    print()
t = int(input())
for case in range(t):
    n, m = list(map(int,input().split()))
    arr = [list() for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int,input().split()))

    (sol(arr, n, m))
