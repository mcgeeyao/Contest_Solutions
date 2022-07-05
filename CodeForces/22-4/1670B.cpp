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
    while (t--){
        int n, k, res;
        char c;
        string s;
        cin >> n >> s >> k;
        vector<bool> sets(26,false);
        while (k--){
            cin >> c;
            sets[int(c) - int('a')] = true;
        }
        int last = 0;
        res = 0;
        for (int i = 0; i < n; ++i){
            if (sets[int(s[i]) - int('a')]){
                res = max(res, i - last);
                last = i;
            }
        }
        cout << res << endl;
    }
    
    return 0;
}