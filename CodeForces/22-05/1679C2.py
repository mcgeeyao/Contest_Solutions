import sys
input = sys.stdin.readline
  
    
            
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
            self.los[ind] = lo
            self.his[ind] = hi
            return
    
        mid = (lo + hi) // 2
        left = (ind << 1) + 1
        right = (ind << 1) + 2
        self.build(left, lo, mid)
        self.build(right, mid + 1, hi)
        self.Nodes[ind] = self.Nodes[left] + self.Nodes[right]
        self.los[ind] = lo
        self.his[ind] = hi
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
            self.Nodes[ind] = val * (hi - lo + 1)
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
        
            
        
        
        
            
        
        
        

n, q = list(map(int,input().split()))
v = [0] * n
h = [0] * n
v_tree = Segment_Tree(v)
h_tree = Segment_Tree(h)
for _ in range(q) :
    qu = list(map(int,input().split()))
    if qu[0] == 1:
        v[qu[2] - 1] += 1
        h[qu[1] - 1] += 1
        v_tree.update(1, qu[2] - 1)
        h_tree.update(1, qu[1] - 1)

    elif qu[0] == 2:
        v[qu[2] - 1] -= 1
        h[qu[1] - 1] -= 1
        if v[qu[2] - 1] == 0:
            v_tree.update(0, qu[2] - 1)
        if h[qu[1] - 1] == 0:
            h_tree.update(0, qu[1] - 1)
        
    else:
        x1, y1 = qu[1], qu[2]
        x2, y2 = qu[3], qu[4]
        h_check = h_tree.query_sum(x1 - 1, x2 - 1) == x2 - x1 + 1
        v_check = v_tree.query_sum(y1 - 1, y2 - 1) == y2 - y1 + 1
        if v_check or h_check:
            print('Yes')
        else:
            print('NO')
        
        