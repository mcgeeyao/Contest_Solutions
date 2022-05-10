#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#define ll long long
using namespace std;



int main(){
    cout.sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        ll n, res, x, m, l, r, tmp, curr;
        cin >> n;
        vector<int> arr, arr2;
        int p = n;
        while (p--) {
            cin>>x;
            arr.push_back(x);
            arr2.push_back(x);
        }
        vector<vector<int> > dp(n, vector<int> (n));
        for (int mid = n-2; mid > 1; --mid) {
            tmp = 0;
            for (int j = 0; j < mid-1; j++) {
                l = mid+1;
                r = n-1;
                while (l <= r) {
                    m = (l+r)/2;
                    if (arr2[m] < arr2[mid-j-1])
                        l = m + 1;
                    else
                        r = m - 1;
                }
                tmp += r - mid;
                dp[mid-j-1][mid] = tmp;
            }
            curr = mid;
            while (curr < n-1 && arr2[curr] > arr2[curr+1]){
                tmp = arr2[curr];
                arr2[curr] = arr2[curr+1];
                arr2[curr+1] = tmp;
                curr += 1;
            }
        }
        res = 0;
        for (int i = 0; i < n-3; i++) {
            for (int j = i+2; j < n-1; j++){
                if (arr[i]<arr[j])
                    res += dp[i+1][j];
            }
        }
        cout << res << endl;
    }
    
    return 0;
}