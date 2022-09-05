import sys
input = sys.stdin.readline
from bisect import bisect_left
t = int(input())
for _ in range(t):
    n = int(input())
    a = [sorted(map(int, input().split()))]
    b = [sorted(map(int, input().split()))]
    res = 0
    for i in range(29, -1, -1):
        mask = 1 << i
        check = True
        m = len(a)
        Num = []
        for j in range(m):
            aNum = len(a[j]) - bisect_left(a[j], mask)
            bNum = bisect_left(b[j], mask)
            if aNum != bNum:
                check = False
                break
            else:
                Num.append(aNum)
        if check:
            res |= mask
            for j in range(m):
                a.append(([num - mask for num in a[j][len(a[j])-Num[j]:]]))
                a[j] = a[j][:len(a[j])-Num[j]]
                b.append(b[j][:Num[j]])
                b[j] = ([num - mask for num in b[j][Num[j]:]])
        else:
            for j in range(m):
                for k in range(len(a[j])-1 , -1, -1):
                    if a[j][k] & mask:
                        a[j][k] -= mask
                    else:
                        break
                a[j].sort()
                for k in range(len(b[j])-1 , -1, -1):
                    if b[j][k] & mask:
                        b[j][k] -= mask
                    else:
                        break
                b[j].sort()
    print(res)