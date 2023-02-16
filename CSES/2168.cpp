// 2168. Nested Ranges check
// Accept


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
#define MP make_pair
#define F first
#define S second

using namespace std;



// Binary Index Tree
template<typename valueType>
class BIT {
private:
    vector<valueType> nums;
    vector<valueType> sums;
    valueType n;
public:
    BIT(valueType len) {
        n = len;
        nums.resize(n + 1, 0);
        sums.resize(n + 1, 0);
    }

    BIT(vector<valueType> arr) {
        n = arr.size();
        nums.resize(n + 1, 0);
        sums.resize(n + 1, 0);
        for(int i = 0; i < n + 1; ++i) Update(i, arr[i]);
    }

    bool Update(valueType ind, valueType val) {
        if (ind < 0 || ind >= n) return false;
        ind++;
        valueType diff = nums[ind] - val;
        nums[ind] = val;
        while (ind <= n) {
            sums[ind] -= diff;
            ind += (ind & -ind);
        }
        return true;
    }

    valueType Query(valueType ind) {
        if (ind < 0 || ind >= n) return 0;
        ind++;
        valueType sum = 0;
        while (ind > 0) {
            sum += sums[ind];
            ind -= (ind & -ind);
        }
        return sum;
    }

    valueType Query(valueType left, valueType right) {return Query(right) - Query(left - 1);}
};

void sol(vector<pii> arr, int n) {
    vector<pii> sortx(n), sorty(n);
    vector<int> res1(n), res2(n);
    unordered_map<int, int> d;
    BIT<int> bit(n);
    int l, r, mid, idx, yi;

    for (int i = 0; i < n; ++i) {
        sortx[i] = MP(arr[i].F, i);
        sorty[i] = MP(arr[i].S, i);
    }
    sort(sortx.begin(), sortx.end(), [&arr](pii &x1, pii &x2){
        return (arr[x1.S].F < arr[x2.S].F || arr[x1.S].F == arr[x2.S].F && arr[x1.S].S > arr[x2.S].S);
        } );
    sort(sorty.begin(), sorty.end());

    for (int i = 0; i < n; ++i) {
        d[sorty[i].S] = i;
    }

    for (int i = 0; i < n; ++i) {
        idx = sortx[i].S;
        yi = arr[idx].S;

        l = 0;
        r = n - 1;
        while (l <= r) {
            mid = (l + r) >> 1;
            if (sorty[mid].F <= yi) l = mid + 1;
            else r = mid - 1;
        }
        res1[idx] = r + 1 - bit.Query(0, r) - 1 > 0;
        
        l = 0;
        r = n - 1;
        while (l <= r) {
            mid = (l + r) >> 1;
            if (sorty[mid].F < yi) l = mid + 1;
            else r = mid - 1;
        }    
        res2[idx] = bit.Query(l, n - 1) > 0;

        bit.Update(d[idx], 1);
    }
    for (int i = 0; i < n; ++i) {
        cout << res1[i] << ' ';
    }
    cout << endl;
    for (int i = 0; i < n; ++i) {
        cout << res2[i] << ' ';
    }
    cout << endl;
}

int main() {
    cout.sync_with_stdio(false);
    cin.tie(nullptr);

    int n, res, x, y;
    cin >> n;
    vector<pii> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> x, cin >> y;
        arr[i] = MP(x, y);
    }
    sol(arr, n);
    // cout << res << endl;

    return 0;
}
