import sys
input = sys.stdin.readline
def sol(arr, n):
    pass
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    s = input()
    print(sol(arr, n))

# Binary Index Tree
class BIT:
    def __init__(self, n):
        self.n = n
        self.nums = [0] * (n + 1)
        self.sums = [0] * (n + 1)

    def update(self, ind, val):
        ind += 1
        diff = self.nums[ind]-val
        self.nums[ind] = val
        while (ind <= self.n):
            self.sums[ind] -= diff
            ind += (ind & -ind)
        return True

    def query(self, ind):
        ind += 1
        total=0
        while (ind > 0):
            total += self.sums[ind]
            ind -= (ind & -ind)
        return total

    def sum(self, l, r):
        return self.query(r) - self.query(l-1)
    
# Disjoint Set
class DJS:
    def __init__(self, n):
        self.arr = [0] * n
        self.rank = [1] * n
    
    def find(self, x):
        if x != self.arr[x]:
            self.arr[x] = self.find(self.arr[x])
        return self.arr[x]
    
    def union(self, x, y):
        xp = self.find(x)
        yp = self.find(y)
        if self.rank[xp] >= self.rank[yp]:
            self.arr[yp] = xp
            self.rank[xp] += 1
        else:
            self.arr[xp] = yp
            self.rank[yp] += 1
            
        