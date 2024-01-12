#include <iostream>
#include <vector>
#include <algorithm>

#define pii pair<int, int>
#define PB push_back
#define MP make_pair

using namespace std;

int main() {
    cout.sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k, i, j, cnt = 0;
    string s;
    cin >> n;
    vector<pii> arr;
    vector<int> res(n, 0), empt;
    for (i = 0; i < n; ++i) {
        cin >> j >> k;
        arr.PB(MP(j, i));
        arr.PB(MP(k, i + n));
    }
    sort(arr.begin(), arr.end());
    for (auto &[j, i]: arr) {
        if (i < n && res[i] == 0)
            if (empt.empty()) res[i] = ++cnt;
            else res[i] = empt.back(), empt.pop_back();
        else empt.PB(res[i - n]);
    }
    cout << cnt << '\n';
    for (auto &i: res)
        cout << i << ' ';

    return 0;
}
