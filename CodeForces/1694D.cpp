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
int res;
vector<int> dfs(int v, vector<unordered_set<int> > adj, vector<int> l, vector<int> r) {
    cout << v << ' ' << res << endl;
    if (adj[v].empty()) {
        if (l[v]) {
            res++;
            return (vector<int>) {l[v], r[v]};
        }
        return (vector<int>) {0, 0};
    }
    int cl = 0, cr = 0;
    for (auto u: adj[v]) {
        vector<int> tmp = dfs(u, adj, l, r);
        cl += tmp[0];
        cr += tmp[1];
    }
    if (cr < l[v]) {
        res++;
        return (vector<int>) {l[v], r[v]};
    }
    if (cl > r[v]) {
        return (vector<int>) {l[v], r[v]};
    }
    return (vector<int>) {max(l[v], cl), min(r[v], cr)};
}



int main() {
    cout.sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        int n, k, tmp;
        char c;
        string s;
        cin >> n;
        vector<unordered_set<int> > adj(n, unordered_set<int> ());
        vector<int> arr(n), l(n), r(n);
        for (int i = 1; i < n; ++i) {
            cin >> arr[i];
            adj[arr[i] - 1].insert(i);
        }
        for (int i = 0; i < n; ++i) {
            cin >> l[i];cin >> r[i];
        }
        res = 0;
        dfs(0, adj, l, r);
        cout << res << endl;
    }
    return 0;
}


