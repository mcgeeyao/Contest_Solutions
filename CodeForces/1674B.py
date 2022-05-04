
def sol(s):
    first = ord(s[0]) - ord('a')
    sec = ord(s[1]) - ord('a')
    if first < sec:
        return (first)*25 + sec
    else:
        return (first)*25 + sec+1
    
t=int(input())
for case in range(t):
    s = input()
    print(sol(s))