def sol(s, n, k):
    if k >= 25 :
        return 'a' * n
    
    toa = ord('a')
    tosec = -1
    tosec2 = -1
    sec = ''
    res = ''
    for i in range(n):
        tmp = ord(s[i]) 
        if tmp <= toa :
            res += 'a'
        elif tmp - toa <= k :
            k -= tmp - toa
            toa = tmp
            res += 'a'
        elif k > 0 :
            tosec = tmp 
            tosec2 = tosec - k
            sec = chr(tmp - k)
            k = 0
            res += sec
        else :
            if tosec2 <= tmp <= tosec:
                res += sec
            else:
                res += s[i]
    return res
    
t = int(input())
for case in range(t):
    n, k = list(map(int,input().split()))
    s = input()
    print(sol(s, n, k))