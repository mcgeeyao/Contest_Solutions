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

    int n, k;
    ll res = 1;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) cin >> arr[i];
    sort(arr.begin(), arr.end());
    for (int &i: arr) {
        if (i > res) break;
        else res += i;
    }

    cout << res << endl;
    return 0;
}

