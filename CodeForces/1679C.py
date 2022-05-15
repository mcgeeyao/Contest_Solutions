import sys
input = sys.stdin.readline

class Binary_Index_Tree:
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
 

n, q = list(map(int,input().split()))
v = [0] * n
h = [0] * n
v_tree = Binary_Index_Tree(n)
h_tree = Binary_Index_Tree(n)
for _ in range(q) :
    qu = list(map(int,input().split()))
    if qu[0] == 1:
        v[qu[2] - 1] += 1
        h[qu[1] - 1] += 1
        v_tree.update(qu[2] - 1, 1)
        h_tree.update(qu[1] - 1, 1)

    elif qu[0] == 2:
        v[qu[2] - 1] -= 1
        h[qu[1] - 1] -= 1
        if v[qu[2] - 1] == 0:
            v_tree.update(qu[2] - 1, 0)
        if h[qu[1] - 1] == 0:
            h_tree.update(qu[1] - 1, 0)
        
    else:
        x1, y1 = qu[1], qu[2]
        x2, y2 = qu[3], qu[4]
        h_check = h_tree.sum(x1 - 1, x2 - 1) == x2 - x1 + 1
        v_check = v_tree.sum(y1 - 1, y2 - 1) == y2 - y1 + 1
        if v_check or h_check:
            print('Yes')
        else:
            print('NO')
        
        