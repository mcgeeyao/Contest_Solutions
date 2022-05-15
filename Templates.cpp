
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>

#define ll long long
#define pii pair<int, int>

using namespace std;

int main(){
    cout.sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--){
        int n, k, res;
        ll l;
        char c;
        string s;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; ++i) cin >> arr[i];

        cout << res << endl;
    }
    return 0;
}


// Binary Index Tree
template<typename valueType>
class BIT{
    private:
        vector<valueType> nums;
        vector<valueType> sums;
        valueType n;
    public:
        BIT(valueType len){
            n = len;
            nums = vector<valueType> (len + 1, 0);
            sums = vector<valueType> (len + 1, 0);
        }

        bool Update(valueType ind, valueType val){
            if (ind < 0 || ind >= n) return false;
            ind++;
            valueType diff = nums[ind] - val;
            nums[ind] = val;
            while (ind <= n){
                sums[ind] -= diff;
                ind += (ind & -ind);
            }
            return true;
        }

        valueType Query(valueType ind){
            if (ind < 0 || ind >= n) return 0;
            ind++;
            valueType sum = 0;
            while (ind > 0){
                sum += sums[ind];
                ind -= (ind & -ind);
            }
            return sum;
        }
};


// Disjoint Set
template<typename valueType>
class DJS{
    private:
        vector<valueType> arr;
        vector<valueType> rank;
    
    public:
        DJS(valueType len){
            arr = vector<valueType> (len, 0);
            rank = vector<valueType> (len, 1);
        }

        valueType Find(valueType x){
            if (arr[x] != x)
                arr[x] = find(arr[x]);
            return arr[x];
        }

        valueType Union(valueType x, valueType y){
            valueType xp = find(x);
            valueType yp = find(y);
            if (rank[xp] >= rank[yp]){
                arr[yp] = xp;
                rank[xp]++;
            } else {
                arr[xp] = yp;
                rank[yp] ++;
            }
        }
};