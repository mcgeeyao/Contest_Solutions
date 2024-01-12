


#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long

using namespace std;


bool check(ll t, vector<int> &arr, int k) {
    ll curr = 0;
    int cnt = 1;
    for (int i: arr) {
        curr += i;
        if (curr > t) {
            cnt += 1;
            curr = i;
        }
        if (cnt > k) return false;
    }
    return true;
}

int main() {

    int n, k, i, a;
    cin >> n >> k;
    ll l = 0, r = 0, mid;
    vector<int> arr(n);
    for (i = 0; i < n; ++i) {
        cin >> arr[i];
        r += arr[i];
        l = max(l, (ll)arr[i]);
    }
    while (l <= r) {
        mid = l + (r - l) / 2;
        if (check(mid, arr, k)) r = mid - 1;
        else l = mid + 1;
    }
    cout << l << "\n";
}