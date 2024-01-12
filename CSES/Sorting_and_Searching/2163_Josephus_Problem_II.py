import sys
input = sys.stdin.readline

class BIT:
    def __init__(self, n):
        self.n = n
        self.nums = [0] * (n + 1)
        self.sums = [0] * (n + 1)

    def update(self, ind, val):
        ind += 1
        diff = self.nums[ind] - val
        self.nums[ind] = val
        while (ind <= self.n):
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
        return self.sums[ind]
def sqrt(n):
    l = 0
    r = n
    while l <= r:
        mid = (l + r) >> 1
        if mid * mid < n:
            l = mid + 1
        else:
            r = mid - 1

def sol(n, k):
    if n == 1:
        print(1)
        return 
    bit = BIT(n)
    for i in range(n):
        bit.update(i, 1)
    LOGN = 1
    tmp = n
    while tmp:
        tmp >>= 1
        LOGN += 1
    curr = k % n
    for i in range(n):
        print(curr + 1, end=' ')
        tol = n - i
        left = curr + 1 - bit.query(curr)
        tar = (left + k) % tol

        accu = 0
        ind = 0
        for i in range(LOGN, -1,  -1):
            if ind + (1 << i) < n + 1 and accu + bit[ind + (1 << i)] < tar:
                ind += (1 << i)
                accu += bit[ind]
                # print(ind, accu)
        bit.update(curr, 0)
        curr = ind
        
    print(curr + 1)
    
    
n, k = list(map(int,input().split()))
(sol(n, k))