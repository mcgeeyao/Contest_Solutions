class segmentTree():
    def __init__(self, n):
        self.n = n
        self.arr = [0] * (n * 2 + 5)
    def update(self, ind, val):
        self.arr[self.n + ind] = val
        p = self.n + ind
        while p > 0:
            self.arr[(p - 1) // 2] = max(self.arr[p + p % 2], self.arr[p + p % 2 - 1])
            p = (p - 1) // 2
        
    def query(self, left, right):
        l = left + self.n
        r = right + self.n
        tmp = 0
        while l <= r:
            tmp = max(tmp, tmp if l % 2 else self.arr[l], self.arr[r] if r % 2 else tmp)
            l = (l - l % 2) // 2
            r = (r - r % 2 - 1) // 2
        return tmp
    
class segmentTree():
    def __init__(self, n):
        self.n = n
        self.arr = [0] * (n * 2 + 5)
    def update(self, ind, val):
        self.arr[self.n + ind] = val
        p = self.n + ind
        while p > 0:
            self.arr[(p - 1) // 2] = min(self.arr[p + p % 2], self.arr[p + p % 2 - 1])
            p = (p - 1) // 2
        
    def query(self, left, right):
        l = left + self.n
        r = right + self.n
        tmp = 0
        while l <= r:
            tmp = min(tmp, tmp if l % 2 else self.arr[l], self.arr[r] if r % 2 else tmp)
            l = (l - l % 2) // 2
            r = (r - r % 2 - 1) // 2
        return tmp
    
class segmentTree():
    def __init__(self, n):
        self.n = n
        self.arr = [0] * (n * 2 + 5)
    def update(self, ind, val):
        self.arr[self.n + ind] = val
        p = self.n + ind
        while p > 0:
            self.arr[(p - 1) // 2] = self.arr[p + p % 2] + self.arr[p + p % 2 - 1]
            p = (p - 1) // 2
        
    def query(self, left, right):
        l = left + self.n
        r = right + self.n
        tmp = 0
        while l <= r:
            tmp = tmp + (0 if l % 2 else self.arr[l]) + (self.arr[r] if r % 2 else 0)
            l = (l - l % 2) // 2
            r = (r - r % 2 - 1) // 2
        return tmp
    