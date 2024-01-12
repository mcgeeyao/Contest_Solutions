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
    unordered_set<char> st;
    int tmp, i;
    for (i = 0; i < n; ++i) {
        tmp = st.size();
        st.insert(s[i]);
        if (tmp == 3 && st.size() == 4) res += s[i], st.clear();
    }
    for (i = 0; i < 4; ++i) {
        if (st.find(d[i]) == st.end()) {
            res += d[i];
            break;
        }
    }
 
    cout << res << endl;
 
    return 0;
}