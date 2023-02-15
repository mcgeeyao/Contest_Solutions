#include <bits/stdc++.h>
using namespace std;
const int mod = 998244353;
int n, ans, dp[105][105], a[105][105];
int main() {
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
		for (int j = i; j <= n; j++) scanf("%d", &a[i][j]);
	dp[1][1] = 2;
	
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= i; j++) {
			bool flag = 0;
			for (int k = 1; k <= i; k++) {
				if (a[k][i] == 1 && k < j) flag = 1;
				if (a[k][i] == 2 && k >= j) flag = 1;
			}
			if (flag) { dp[i][j] = 0; continue; }
			dp[i + 1][j] = (dp[i][j]) % mod;
			dp[i + 1][i + 1] = (dp[i + 1][i + 1] + dp[i][j]) % mod;
		}
	for (int i = 1; i <= n; i++) ans = (ans + dp[n][i]) % mod;
	printf("%d\n", ans);
}