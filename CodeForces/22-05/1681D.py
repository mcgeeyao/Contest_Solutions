import sys
input = sys.stdin.readline
def get(x):
    l = []
    m = -1
    while x:
        l.append(x%10)
        m = max(m, x%10)
        x //= 10
    return l, m
def sol(n, x):
    
    l, m = get(x)
    if m == 1:
        return -1
    cnt = 0
    qu = [(l, x)]
    while True:
        tmp = []
        for l1, x1 in qu:
            if len(l1) >= n:
                return cnt
            l1 = sorted(l1)[::-1]
            for i in range(min(2, len(l1))):
                if l1[i] >= 2:
                    tmp.append((get(l1[i]*x1)[0], l1[i]*x1))
        cnt += 1
        qu = tmp
    
    

n, x = list(map(int,input().split()))
print(sol(n, x))

int n;
int ans = 1e9;
void dfs(ll x, string s, int now)
{
 if (now + n - s.size() >= ans)
  return;
 if (s.size() == n)
 {
  ans = now;
  return;
 }
 int r = -1;
 vector<int> a(10);
 for (auto c : s)
  a[c - '0'] = 1;
 for (int i = 9; i > 1; i--)
  if (a[i])
  {
   dfs(x * i, to_string(x * i), now + 1);
  }
}
int main()
{
 ios::sync_with_stdio(0);
 cin.tie(0);
 int r = 0;
 ll x;
 cin >> n >> x;
 string s = to_string(x);
 dfs(x, s, 0);
 if (ans == 1'000'000'000)
  ans = -1;
 cout << ans << endl;