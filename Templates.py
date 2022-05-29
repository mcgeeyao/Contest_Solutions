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
        self.arr = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        if x != self.arr[x]:
            self.arr[x] = self.find(self.arr[x])
        return self.arr[x]
    
    def union(self, x, y):
        xp = self.find(x)
        yp = self.find(y)
        if xp != yp:
            if self.rank[xp] >= self.rank[yp]:
                self.arr[yp] = xp
                self.rank[xp] += self.rank[yp]
            else:
                self.arr[xp] = yp
                self.rank[yp] += self.rank[xp]
            
            
            
class Segment_TreeNode():
    def __init__(self, lo, hi, s=0, mi=0, ma=0):
        self.lo = lo
        self.hi = hi
        self.sum = s
        self.min = mi
        self.max = ma
            
class Segment_Tree():
    def __init__(self, arr):
        self.n = len(arr)
        logs = 1
        tmp = self.n - 1
        while tmp:
            logs += 1
            tmp >>= 1
        
        self.Nodes = [0] * ((1 << logs) - 1)
        self.lazy = [0] * ((1 << logs) - 1)
        self.arr = arr
        self.build(0, 0, self.n - 1)
        
    def build(self, ind, lo, hi):
        if lo == hi:
            val = self.arr[lo]
            newNode = Segment_TreeNode(lo, hi, val, val, val)
            self.Nodes[ind] = newNode
            return
    
        mid = (lo + hi) // 2
        left = (ind << 1) + 1
        right = (ind << 1) + 2
        self.build(left, lo, mid)
        self.build(right, mid + 1, hi)
        
        nSum = self.Nodes[left].sum + self.Nodes[right].sum
        nMin = min(self.Nodes[left].min, self.Nodes[right].min)
        nMax = max(self.Nodes[left].max, self.Nodes[right].max)
        
        newNode = Segment_TreeNode(lo, hi, nSum, nMin, nMax)
        self.Nodes[ind] = newNode
        return
    def push_up(self, ind):
        self.Nodes[ind].sum = self.Nodes[(ind << 1) + 1].sum + self.Nodes[(ind << 1) + 2].sum
        self.Nodes[ind].min = min(self.Nodes[(ind << 1) + 1].min, self.Nodes[(ind << 1) + 2].min)
        self.Nodes[ind].max = max(self.Nodes[(ind << 1) + 1].max, self.Nodes[(ind << 1) + 2].max)
        
    def push_down(self, ind):
        if not self.lazy[ind]: return
        self.Nodes[(ind << 1) + 1].sum = self.Nodes[ind].max * (self.Nodes[(ind << 1) + 1].hi - self.Nodes[(ind << 1) + 1].lo + 1)
        self.Nodes[(ind << 1) + 1].max = self.Nodes[ind].max
        self.Nodes[(ind << 1) + 1].min = self.Nodes[ind].min
        
        self.Nodes[(ind << 1) + 2].sum = self.Nodes[ind].max * (self.Nodes[(ind << 1) + 2].hi - self.Nodes[(ind << 1) + 2].lo + 1)
        self.Nodes[(ind << 1) + 2].max = self.Nodes[ind].max
        self.Nodes[(ind << 1) + 2].min = self.Nodes[ind].min
        
        self.lazy[ind] = False
        self.lazy[(ind << 1) + 1] = True
        self.lazy[(ind << 1) + 2] = True
    
    def update(self, val, l, r=-1):
        if r >= 0:
            self._update(0, l, r, val)
        else:
            self._update(0, l, l, val)
        
    def _update(self, ind, l, r, val):
        lo = self.Nodes[ind].lo
        hi = self.Nodes[ind].hi
        if r < lo or l > hi:
            return 
        if l <= lo and r >= hi:
            self.Nodes[ind].sum = val * (hi - lo + 1)
            self.Nodes[ind].min = val
            self.Nodes[ind].max = val
            self.lazy[ind] = True
        else:
            self.push_down(ind)
            self._update((ind << 1) + 1, l, r, val)
            self._update((ind << 1) + 2, l, r, val)
            self.push_up(ind)
    
    def _query(self, ind, l, r):
        lo = self.Nodes[ind].lo
        hi = self.Nodes[ind].hi
        if r < lo or l > hi:
            return 0, 10 ** 18, -10 ** 18
        if l <= lo and r >= hi:
            return self.Nodes[ind].sum, self.Nodes[ind].min, self.Nodes[ind].max
            
        self.push_down(ind)

        s1, mi1, ma1 = self._query((ind << 1) + 1, l, r)
        s2, mi2, ma2 = self._query((ind << 1) + 2, l, r)
        
        s = s1 + s2
        mi = min(mi1, mi2)
        ma = max(ma1, ma2)
            
        return s, mi, ma
    
    def query_max(self, l, r):
        return self._query(0, l, r)[2]
    
    def query_min(self, l, r):
        return self._query(0, l, r)[1]
    
    def query_sum(self, l, r):
        return self._query(0, l, r)[0]
    
    

    
            
class Segment_Tree():
    def __init__(self, arr):
        self.n = len(arr)
        logs = 1
        tmp = self.n - 1
        while tmp:
            logs += 1
            tmp >>= 1
        
        self.Nodes = [0] * ((1 << logs) - 1)
        self.lazy = [None] * ((1 << logs) - 1)
        self.los = [0] * ((1 << logs) - 1)
        self.his = [0] * ((1 << logs) - 1)
        
        self.arr = arr
        
        
        
        self.build(0, 0, self.n - 1)
        
    def build(self, ind, lo, hi):
        if lo == hi:
            val = self.arr[lo]
            self.Nodes[ind] = val
            return
    
        mid = (lo + hi) // 2
        left = (ind << 1) + 1
        right = (ind << 1) + 2
        self.build(left, lo, mid)
        self.build(right, mid + 1, hi)
        self.Nodes[ind] = self.Nodes[left] + self.Nodes[right]
        return
    def push_up(self, ind):
        self.Nodes[ind] = self.Nodes[(ind << 1) + 1] + self.Nodes[(ind << 1) + 2]
        
    def push_down(self, ind):
        if self.lazy[ind] == None: return
        self.Nodes[(ind << 1) + 1] = self.lazy[ind] * (self.his[(ind << 1) + 1] - self.los[(ind << 1) + 1] + 1)
        self.Nodes[(ind << 1) + 2] = self.lazy[ind] * (self.his[(ind << 1) + 2] - self.los[(ind << 1) + 2] + 1)
        self.lazy[ind] = None
    
    def update(self, val, l, r=-1):
        if r >= 0:
            self._update(0, l, r, val)
        else:
            self._update(0, l, l, val)
        
    def _update(self, ind, l, r, val):
        lo = self.los[ind]
        hi = self.his[ind]
        if r < lo or l > hi:
            return 
        if l <= lo and r >= hi:
            self.Nodes[ind].sum = val * (hi - lo + 1)
            self.lazy[ind] = val
        else:
            self.push_down(ind)
            self._update((ind << 1) + 1, l, r, val)
            self._update((ind << 1) + 2, l, r, val)
            self.push_up(ind)
    
    def _query(self, ind, l, r):
        lo = self.los[ind]
        hi = self.his[ind]
        if r < lo or l > hi:
            return 0
        if l <= lo and r >= hi:
            return self.Nodes[ind]
            
        self.push_down(ind)

        s1 = self._query((ind << 1) + 1, l, r)
        s2 = self._query((ind << 1) + 2, l, r)
            
        return s1 + s2
    
    def query_sum(self, l, r):
        return self._query(0, l, r)
        
            
            
        
        
        
            
        
        
        