from heapq import heappush, heappop
import sys
input = sys.stdin.readline
def sol(s, n):
    
    arr = []
    curr = 1
    for i in range(1, n):
        if s[i] == s[i-1]:
            curr += 1
        else:
            arr.append(curr)
            curr = 1
    arr.append(curr)
    res = 0
    secres = len(arr)
    state = False
    curr = 0
    heap = []
    ind = 0
    for i in arr:
        if state :
            if i%2:
                heappush(heap, (i, ind))
                tmp = curr
                cnt = 0
                while tmp>0:
                    x,inds = heappop(heap)
                    left1 = False
                    left2 = False
                    if x<=tmp:
                        if inds == 0 :   
                            left1 = True
                            left11 = x
                        elif inds == n-1 :   
                            left2 = True
                            left22 = x
                        else:
                            secres -= 2
                            tmp -=x
                    else:
                        break
                if left1 and tmp>=left11:
                    secres -=1
                    tmp -= left11
                if left2 and tmp>=left22:
                    secres -=1
                        
                heap = []
                res += curr
                curr = 0
                state = False
            else:
                heappush(heap, (i, ind))
                curr += 1
        else:
            if i%2:
                heappush(heap, (i, ind))
                curr = 1
                state = True
        ind += 1
    return str(res) + ' ' + str(secres)
t = int(input())
for case in range(t):
    n = int(input())
    arr = input()
    print(sol(arr, n))