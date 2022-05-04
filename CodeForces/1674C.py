
def sol(s, t):
    if 'a' in t and len(t) > 1:
        return -1
    elif t == 'a':
        return 1
    else:
        return 2**(len(s))
    
t=int(input())
for case in range(t):
    s = input()
    t = input()
    print(sol(s, t))