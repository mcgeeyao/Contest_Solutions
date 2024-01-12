import sys
input = sys.stdin.readline
def sol(arr, n):
    tmp = arr + [10**10]
    st = [-1]
    dp1 = [0] * n
    for i in range(n):
        while st and tmp[st[-1]] < arr[i]: st.pop()
        dp1[i] = st[-1]
        st.append(i)
        
    tmp = arr + [-1]
    st = [n]
    dp2 = [0] * n
    for i in range(n-1, -1, -1):
        while st and tmp[st[-1]] > arr[i]: st.pop()
        dp2[i] = st[-1]
        st.append(i)
    
    # sufmn = [10**10]
    # for i in range(n-1, -1, -1):
    #     sufmn.append(min(sufmn[-1], arr[i]))
    # sufmn = sufmn[::-1]
    
    res = 0
    for i in range(n):
        res += (dp1[i] + 1) * (n - i)
        res += (n - dp2[i]) * (i + 1)
        res -= (dp1[i] + 1) * (n - dp2[i])
        res -= (n - dp2[i])
        mx = 0
        r = n-1
        
        sufmn = [10**10]*n
        for j in range(dp2[i], n):
            sufmn[j] = min(sufmn[j-1], arr[j])
            
        for l in range(i-1, dp1[i], -1):
            mx = max(arr[l], mx)
            while r >= dp2[i] and sufmn[r] < mx:
                r -= 1
            res -= (r - dp2[i] + 1)
            
        
    return res
 
t = int(input())
for case in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sol(arr, n))