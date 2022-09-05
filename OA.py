
def sol(message):
    last = '0'
    first = -1
    res = ['a'] * len(message)
    for i in range(len(message)):
        if message[i] in 'aeiou':
            if last == '0':
                first = i
                last = message[i]
            else:
                res[i] = last
                last = message[i]
    if first >= 0:
        res[first] = last
    ret = ''
    for i in res: ret += i
    return ret

def sol(field):
    n = len(field)
    m = len(field[0])
    for i in range(n):        
        for j in range(m):
            pass  
            
def sol(lamps, points):
    dp = [0] * 100002
    for i, j in lamps:
        dp[i] += 1
        dp[j+1] -= 1
    for i in range(1, 100002):
        dp[i] += dp[i-1]
    res = []
    for i in points:
        res.append(dp[i])
    return res