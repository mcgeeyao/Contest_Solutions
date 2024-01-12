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

using namespace std;

int main() {
    cout.sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    ll l;
    char c;
    string s, res, d = "ACGT";
    cin >> s;
    n = s.length();
    vector<vector<int > > dp(4, vector<int>(n, 100000000)), bt1(4, vector<int>(n, 100000000)), bt2(4, vector<int>(n, 100000000));
    vector<int > arr;
    for (char c: s) {
        if (c == 'A') arr.push_back(0);
        else if (c == 'C') arr.push_back(1);
        else if (c == 'G') arr.push_back(2);
        else arr.push_back(3);
    }
    int i, j, k;
    for (i = 0; i < 4; ++i) {
        dp[i][0] = 1;
        if (arr[0] == i) dp[i][0] += 1;
    }
    for (i = 1; i < n; ++i) {
        for (j = 0; j < 4; ++j) {
            for (k = 0; k < 4; ++k) {
                if (dp[k][i-1] + (k != j || j == k && k == arr[i]) < dp[j][i]) {
                    bt1[j][i] = k;
                    bt2[j][i] = (k != j || j == k && k == arr[i]);
                }
                dp[j][i] = min(dp[j][i], dp[k][i-1] + (k != j || j == k && k == arr[i]));
            }
        }
    }
    
    int curr, mn = 100000000;
    for (i = 0; i < 4; ++i) {
        if (dp[i][n-1] <= mn) {
            mn = dp[i][n-1];
            curr = i;
        }
            
    }
    int ind = n - 1;
    while (ind >= 0) {
        if (bt2[curr][ind])   
            res += d[curr];
        curr = bt1[curr][ind];
        ind--;
    }

    reverse(res.begin(), res.end());
    cout << res << endl;

    return 0;
}