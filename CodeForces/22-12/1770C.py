import sys
input = sys.stdin.readline

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
def sol(arr, n):
    if len(set(arr)) != len(arr): return 'NO'
    for i in range(len(primes)):
        md = [0] * primes[i]
        for j in arr:
            md[j % primes[i]] += 1
        check = True
        for j in md:
            if j <= 1:
                check = False
                break
        if check:
            return 'NO'
    return 'YES'

t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))
