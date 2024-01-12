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
 
    int n, m, x, y;
    ll l;
    char c;
    string s, res;
    cin >> n >> m;
    for (int i = 0; i < m; ++i) {
        cin >> x >> y;
        cout << min(x, y) << " " << max(x, y) << "\n";
    }
 
    return 0;
}
