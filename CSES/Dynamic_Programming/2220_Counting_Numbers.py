
def cnt(a):
    ad = []
    if a == 0: ad = [0]
    else:
        while a:
            ad.append(a%10)
            a //= 10
    ad = ad[::-1]
    n = len(ad)
    
    res = (ad[0]-1) * pow(9, n-1)
    for i in range(1, n):
        res += (ad[i] - (ad[i] > ad[i-1])) * pow(9, n-i-1)
        if ad[i] == ad[i-1]: break
        
    for i in range(1, n):
        res += pow(9, n-i)
    return res

def sol(a, b):
    return cnt(b + 1) - cnt(a)

a, b = list(map(int, input().split()))
print(sol(a, b))