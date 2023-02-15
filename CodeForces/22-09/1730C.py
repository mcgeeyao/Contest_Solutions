import sys
input = sys.stdin.readline
def sol(arr, n):
    res = [0] * 10
    mn = 10
    for i in arr[::-1]:
        if i <= mn:
            mn = i
            res[i] += 1
        else:
            res[min(i + 1, 9)] += 1
    ret = ''
    for i in range(10):
        ret += str(i) * res[i]
    return ret
 
t = int(input())
for case in range(t):
    s = input()[:-1]
    arr = [int(i) for i in s]
    n = len(arr)
    print(sol(arr, n))
