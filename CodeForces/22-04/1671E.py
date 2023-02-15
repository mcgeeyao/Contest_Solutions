

def dfs(tree,i,h):
    if i>=2**(h-1)-1:
        return [tree[i],1]
    ls,li=dfs(tree,i*2+1,h)
    rs,ri=dfs(tree,i*2+2,h)
    res=li*ri
    if ls!=rs:
        res*=2
    if ls>rs:
        return [tree[i]+rs+ls,res]
    else:
        return [tree[i]+ls+rs,res]


h=int(input())
tree=input()
print(dfs(tree,0,h)[1]%998244353)
