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

// Disjoint Set
template<typename valueType>
class DJS {
private:
    vector<valueType> arr;
    vector<valueType> rank;

public:
    DJS(valueType len) {
        arr.resize(len);
        for (valueType i = 0; i < len; ++i) arr[i] = i;
        rank.resize(len, 1);
    }

    valueType Find(valueType x) {
        if (arr[x] != x)
            arr[x] = Find(arr[x]);
        return arr[x];
    }

    valueType Union(valueType x, valueType y) {
        valueType xp = Find(x);
        valueType yp = Find(y);
        if (xp != yp) {
            if (rank[xp] >= rank[yp]) {
                arr[yp] = xp;
                rank[xp] += rank[yp];
            } else {
                arr[xp] = yp;
                rank[yp] += rank[xp];
            }
        }
    }
};