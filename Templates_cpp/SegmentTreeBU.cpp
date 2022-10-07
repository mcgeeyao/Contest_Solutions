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

using namespace std;


template<typename valueType>         
class Segment_Tree {
private:
    int n;
    vector<valueType> arr;
public:

    Segment_Tree(int num) {
        n = num;
        arr.resize(2 * n + 5, 0);
    }

    void update(int l, int r, valueType val) {
        int p = self.n + ind
        arr[p] = val;
        while (p > 0) {
            arr[(p - 1) / 2] = max(arr[p + p % 2], arr[p + p % 2 - 1]);
            p = (p - 1) / 2;
        }
    }

    valueType query(int l, int r) {
        int l = left + n;
        int r = right + n;
        valueType tmp = 0;
        while (l <= r) {
            tmp = max(tmp, tmp * (l % 2) + arr[l] * (1 - l % 2), arr[r] * (r % 2) + tmp * (1 - r % 2));
            l = (l - l % 2) / 2;
            r = (r - r % 2 - 1) / 2;
        }
        return tmp;
    }

    valueType& operator[](int num) {return *arr[n + num];}

};