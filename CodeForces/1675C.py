def sol(s):
    
    first = 0
    while first < len(s) and s[first] != '0':
        first += 1
        
    last = len(s) - 1
    while last >= 0 and s[last] != '1':
        last -= 1
        
    if last == -1 and first == len(s):
        return len(s)
    if last == -1 :
        return first + 1
    if first == len(s) :
        return len(s) - last
    return first - last + 1
    
    
            
    
t = int(input())
for case in range(t):
    s = input()
    print(sol(s))