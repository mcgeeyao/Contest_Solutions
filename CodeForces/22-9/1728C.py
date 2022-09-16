import sys
from collections import defaultdict
input = sys.stdin.readline
rand = 0b0101011100101000101011010101111


def cntDig(n):
    cnt = 0
    tmp = n
    while tmp:
        cnt += 1
        tmp //= 10
    return cnt
def sol(a, b, n):
    res = 0
    bst = defaultdict(int)
    for i in b: bst[i^rand] += 1
    
    cnta = [0] * 10
    cntb = [0] * 10
    for i in a:
        if bst[i^rand]: bst[i^rand] -= 1
        elif i > 9:
            cnta[cntDig(i)] += 1
            res += 1
        else:
            cnta[i] += 1
    for i in b:
        if bst[i^rand]: 
            if i > 9:
                cntb[cntDig(i)] += 1
                res += 1
            else:
                cntb[i] += 1
            bst[i^rand] -= 1
    for i in range(2, 10):
        res += abs(cnta[i] - cntb[i])
    return res
        
        
 
t = int(input())
for case in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(sol(a, b, n))
