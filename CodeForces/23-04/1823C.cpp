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

int main() {
    cout.sync_with_stdio(false);
    cin.tie(nullptr);
    int mx = 1e7 + 1;
    vector<int> prime(mx, 0);
    for (int i = 2; i < mx; ++i) {
        if (prime[i] != 0) continue;
        for (int j = i; j < mx; j += i) prime[j] = i;
    }
    int t;
    cin >> t;
    while (t--) {
        int n, k, res = 0, mx = 0, one = 0;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; ++i) {
            cin >> arr[i]; 
            mx = max(mx, arr[i] + 1);
        }

        unordered_map<int, int> d;
        for (auto i: arr) {
            while (i != prime[i]) {
                d[prime[i]]++;
                i /= prime[i];
            }
            d[prime[i]]++;
        }

        for (auto &[a, b]: d) {
            res += b / 2;
            one += b % 2;
            if (one == 3) {
                res++;
                one = 0;
            }
        }

        cout << res << endl;
    }
    return 0;
}

// g++ -std=c++17 CSES/2168.cpp -o cses.out   
