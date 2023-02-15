
def sol(s):
    alpha = set()
    for i in s:
        alpha.add(i)
        
    order = ''
    ind = 0
    while ind<len(s) and alpha:
        if s[ind] in alpha:
            alpha.remove(s[ind])
            order += s[ind]
            ind += 1
        else:
            return 'NO'
    
    ind = 0
    for i in s:
        if i == order[ind]:
            ind += 1
            ind %=len(order)
        else:
            return 'NO'
    return 'YES'

t=int(input())
for case in range(t):
    s = input()
    print(sol(s))