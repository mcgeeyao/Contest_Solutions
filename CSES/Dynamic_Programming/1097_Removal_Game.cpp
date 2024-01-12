#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#include <tuple>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <limits>

#define ll long long
#define pii pair<int, int>
#define PB push_back
#define MP make_pair

using namespace std;
bool stoneGame(vector<int>& p) {
        vector<int> dp = p;
        for (int d = 1; d < p.size(); d++)
            for (int i = 0; i < p.size() - d; i++)
                dp[i] = max(p[i] - dp[i + 1], p[i + d] - dp[i]);
        return dp[0];
    }
int main() {
    cout.sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        int n, k, res, s;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; ++i) cin >> arr[i], s += arr[i];

        cout << res << endl;
    }
    return 0;
}