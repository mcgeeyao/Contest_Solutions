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