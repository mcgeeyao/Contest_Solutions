
def sol(s):
    if len(s) == 1:
        a = ord(s[0]) - ord('a') + 1
        return (f'Bob {a}')
    else:
        if len(s)%2:
            res = 0
            for i in range(1, len(s)-1):
                res += ord(s[i]) - ord('a') + 1
            res += abs(ord(s[-1]) - ord(s[0]))
            return (f'Alice {res}')
        else:
            res = 0
            for i in range(len(s)):
                res += ord(s[i]) - ord('a') + 1
            return (f'Alice {res}')
        

t=int(input())
for case in range(t):
    s = input()
    print(sol(s))