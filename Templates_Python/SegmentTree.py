# Segment Tree        
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
            self.Nodes[ind] = Segment_TreeNode(lo, hi, self.arr[lo], self.arr[lo], self.arr[lo])
            return
    
        mid = (lo + hi) // 2
        left = (ind << 1) + 1
        right = (ind << 1) + 2
        self.build(left, lo, mid)
        self.build(right, mid + 1, hi)
        
        self.Nodes[ind] = Segment_TreeNode(lo, hi)
        self.push_up(ind)
    
    def push_up(self, ind):
        left = (ind << 1) + 1
        right = (ind << 1) + 2
        self.Nodes[ind].sum = self.Nodes[left].sum + self.Nodes[right].sum
        self.Nodes[ind].min = min(self.Nodes[left].min, self.Nodes[right].min)
        self.Nodes[ind].max = max(self.Nodes[left].max, self.Nodes[right].max)
        
    def push_down(self, ind):
        if not self.lazy[ind]: return
        left = (ind << 1) + 1
        right = (ind << 1) + 2
        self.Nodes[left].sum = self.Nodes[ind].max * (self.Nodes[left].hi - self.Nodes[left].lo + 1)
        self.Nodes[left].max = self.Nodes[ind].max
        self.Nodes[left].min = self.Nodes[ind].min
        
        self.Nodes[right].sum = self.Nodes[ind].max * (self.Nodes[right].hi - self.Nodes[right].lo + 1)
        self.Nodes[right].max = self.Nodes[ind].max
        self.Nodes[right].min = self.Nodes[ind].min
        
        self.lazy[ind] = False
        self.lazy[left] = True
        self.lazy[right] = True
    
    def update(self, l, r, val):
        self._update(0, l, r, val)
        
    def _update(self, ind, l, r, val):
        lo = self.Nodes[ind].lo
        hi = self.Nodes[ind].hi
        left = (ind << 1) + 1
        right = (ind << 1) + 2
        if r < lo or l > hi:
            return 
        if l <= lo and r >= hi:
            self.Nodes[ind].sum = val * (hi - lo + 1)
            self.Nodes[ind].min = val
            self.Nodes[ind].max = val
            self.lazy[ind] = True
        else:
            self.push_down(ind)
            self._update(left, l, r, val)
            self._update(right, l, r, val)
            self.push_up(ind)
    
    def _query(self, ind, l, r):
        lo = self.Nodes[ind].lo
        hi = self.Nodes[ind].hi
        left = (ind << 1) + 1
        right = (ind << 1) + 2
        if r < lo or l > hi:
            return 0, 10 ** 18, -10 ** 18
        if l <= lo and r >= hi:
            return self.Nodes[ind].sum, self.Nodes[ind].min, self.Nodes[ind].max
            
        self.push_down(ind)

        s1, mi1, ma1 = self._query(left, l, r)
        s2, mi2, ma2 = self._query(right, l, r)
            
        return s1 + s2, min(mi1, mi2), max(ma1, ma2)
    
    def query_max(self, l, r):
        return self._query(0, l, r)[2]
    
    def query_min(self, l, r):
        return self._query(0, l, r)[1]
    
    def query_sum(self, l, r):
        return self._query(0, l, r)[0]
    
    
