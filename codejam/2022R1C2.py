
def sol(arr, n, k):
    B = 0
    S = 0
    for i in arr:
        B += i * i
        S += i
    A = S * S
    tmp = B - A
    if S == 0 and  B == 0:
        return 0

    if k == 1 :    
        if S == 0:
            return ('IMPOSSIBLE')
        if tmp % (2 * S) != 0 :
            return ('IMPOSSIBLE')
        else:
            return (tmp // (2*S))
    else:
        if tmp % (2 * S) == 0:
            return (tmp // (2*S))
        else:
            res1 = -S + 1
            tmp -= 2 * S * res1
            if tmp%2:
                return ('IMPOSSIBLE')
            else:
                return str(res1) + ' ' + str(tmp // 2)

t=int(input())
for case in range(t):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(f'Case #{case+1}: {sol(arr, n, k)}')