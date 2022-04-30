
def sol(arr,n):
    usedleft = dict()
    usedright = dict()
    used = set()
    usedmid = set()
    usedall = dict(list())
    
    for i, s in enumerate(arr):
        ind1 = 0
        ind2 = len(s)-1
        while ind1 < len(s) - 1 and s[ind1] == s[ind1 + 1]:
            ind1 += 1
        while ind2 > 0 and s[ind2] == s[ind2 - 1]:
            ind2 -= 1
            
        if ind1 == len(s) - 1:
            if s[0] in usedmid:
                return 'IMPOSSIBLE'
            used.add(s[0])
            if s[0] in usedall:
                usedall[s[0]].append(i)
            else:
                usedall[s[0]] = [i]
            continue
        if s[0] == s[-1]:
            return 'IMPOSSIBLE'
        if s[0] in usedleft or s[0] in usedmid:
            return 'IMPOSSIBLE'
        usedleft[s[0]] = i
        used.add(s[0])
        
        
        if s[-1] in usedright or s[-1] in usedmid:
            return 'IMPOSSIBLE'
        usedright[s[-1]] = i
        used.add(s[-1])
        
        for j in range(ind1+1, ind2):
            if s[j] in used and s[j] != s[j - 1]:
                return 'IMPOSSIBLE'
            used.add(s[j])
            usedmid.add(s[j])
            

    useds1 = set()
    for i, s in enumerate(arr):
        path = set()
        if s[0] == s[-1] or i in useds1:
            continue
        useds1.add(i)
        path.add(s[0])
        path.add(s[-1])
        tail = s[-1]
        while tail in usedleft:
            useds1.add(usedleft[tail])
            tail = arr[usedleft[tail]][-1]
            if tail in path:
                return 'IMPOSSIBLE'
            path.add(tail)
        
    
    useds = set()
    res = ''
    for i, s in enumerate(arr):
        ind1 = 0
        while ind1 < len(s) - 1 and s[ind1] == s[ind1 + 1]:
            ind1 += 1
        if ind1 == len(s) - 1:
            continue
        if i in useds:
            continue
        
        useds.add(i)
        tmp = str(s)
        head = s[0]
        while head in usedright or head in usedall:
            if head in usedall:
                for j in usedall[head]:
                    if j not in useds:
                        tmp = arr[j] + tmp
                        useds.add(j)
            if head in usedright:
                tmp = arr[usedright[head]] + tmp
                useds.add(usedright[head])
                head = arr[usedright[head]][0]
            else:
                break
        tail = s[-1]
        while tail in usedleft or tail in usedall:
            if tail in usedall:
                for j in usedall[tail]:
                    if j not in useds:
                        tmp += arr[j] 
                        useds.add(j)
            if tail in usedleft and usedleft[tail] not in useds:
                tmp += arr[usedleft[tail]]
                useds.add(usedleft[tail])
                tail = arr[usedleft[tail]][-1]
            else:
                break
        res += tmp
    sor = []
    for i in range(len(arr)):
        if i not in useds:
            sor.append(arr[i])
    for i in sorted(sor):
        res += i   
    return res 
            
            
    


t=int(input())
for case in range(t):
    n = int(input())
    arr = list(input().split())
    print(f'Case #{case+1}: {sol(arr,n)}')