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
            