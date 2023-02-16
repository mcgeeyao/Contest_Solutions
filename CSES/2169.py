# 2169. Nested Ranges Count
# TLE for pypy

import sys
input = sys.stdin.readline
class BIT:
    def __init__(self, n):
        self.n = n
        self.nums = [0] * (n + 5)
        self.sums = [0] * (n + 5)

    def update(self, ind, val):
        ind += 1
        diff = self.nums[ind] - val
        self.nums[ind] = val
        while (ind <= self.n + 4):
            self.sums[ind] -= diff
            ind += (ind & -ind)
        return True

    def query(self, ind):
        ind += 1
        total = 0
        while (ind > 0):
            total += self.sums[ind]
            ind -= (ind & -ind)
        return total

    def sum(self, l, r):
        return self.query(r) - self.query(l-1)
    
    def __getitem__(self, ind):
        return self.nums[ind + 1]
    
def sol(arr, n):
    sortx = sorted([(arr[ind][0], ind) for ind in range(n)], key=lambda x: (arr[x[1]][0], -arr[x[1]][1]))
    sorty = sorted([(arr[ind][1], ind) for ind in range(n)])
    d = {}
    for i in range(n):
        d[sorty[i][1]] = i
    bit = BIT(n)
    
    res1 = [0] * n
    res2 = [0] * n
    for i in range(n):
        yi = arr[sortx[i][1]][1]
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) >> 1
            if sorty[mid][0] <= yi:
                l = mid + 1
            else:
                r = mid - 1
        res1[sortx[i][1]] = r + 1 - bit.sum(0, r) - 1
        
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) >> 1
            if sorty[mid][0] < yi:
                l = mid + 1
            else:
                r = mid - 1
        res2[sortx[i][1]] = bit.sum(l, n - 1)
        
        bit.update(d[sortx[i][1]], 1)
    for i in res1:
        print(i, end=' ')
    print()
    for i in res2:
        print(i, end=' ')
    # print(res1)
    # print(res2)
                
        
    
    
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
(sol(arr, n))
