import sys
input = sys.stdin.readline
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
    
    def size(self, x):
        return self.rank[self.find(x)]
            
def sol(n, a, b):
    mod = 998244353
    s = set()
    pn = 0
    samei = set()
    for i in range(n):
        if a[i] == b[i]: 
            if a[i] in s:
                return 0
            pn += 1
            s.add(a[i])
            samei.add(i)
    abc = set()      
    while abc:
        abc = set()
        for i in range(n):
            if a[i] != b[i]:
                if a[i] in s:
                    if b[i] in s: return 0
                    s.add(b[i])
                    abc.add(b[i])
                    samei.add(i)
                if b[i] in s:
                    if a[i] in s: return 0
                    s.add(a[i])
                    abc.add(b[i])
                    samei.add(i)
    dg = [0] * (n + 1)
    adj = [set() for _ in range(n + 1)]
    for i in range(n):
        if i not in samei:
            if a[i] not in s:
                dg[a[i]] += 1
                adj[a[i]].add(i)
            if b[i] not in s:
                dg[b[i]] += 1
                adj[b[i]].add(i)
            
    q = set()
    for i in range(1, n + 1):
        if dg[i] == 1:
            q.add(i)
       

    while q:
        nq = set()
        for i in q:
            s.add(i)
            assert(len(adj[i]) == 1)
            if a[[aaa for aaa in adj[i]][0]] != i and a[[aaa for aaa in adj[i]][0]] not in s:
                dg[a[[aaa for aaa in adj[i]][0]]] -= 1
                adj[a[[aaa for aaa in adj[i]][0]]].remove([aaa for aaa in adj[i]][0])
                if dg[a[[aaa for aaa in adj[i]][0]]] == 1:
                    nq.add(a[[aaa for aaa in adj[i]][0]])
                elif dg[a[[aaa for aaa in adj[i]][0]]] == 0:
                     
                    return 0
            if b[[aaa for aaa in adj[i]][0]] != i and b[[aaa for aaa in adj[i]][0]] not in s:
                dg[b[[aaa for aaa in adj[i]][0]]] -= 1
                adj[b[[aaa for aaa in adj[i]][0]]].remove([aaa for aaa in adj[i]][0])
                if dg[b[[aaa for aaa in adj[i]][0]]] == 1:
                    nq.add(b[[aaa for aaa in adj[i]][0]])
                elif dg[b[[aaa for aaa in adj[i]][0]]] == 0:
                    
                    return 0
        q = nq
    djs = DJS(n + 1)
    re = set()
    for i in range(1, n + 1):
        
        if i not in s:
            if dg[i] == 0 or dg[i] > 2:
                return 0
            re.add(i)
            for j in adj[i]:
                djs.union(i, a[j])
                djs.union(i, b[j])
    tmp = set()
    for i in re:
        tmp.add(djs.find(i))
    return (pow(n, pn, mod) * pow(2, len(tmp), mod)) % mod
            

            
            
             
t = int(input())
for case in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(sol(n, a, b))
