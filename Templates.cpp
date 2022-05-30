#include <tuple>
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

// int main() {
//     cout.sync_with_stdio(false);
//     cin.tie(nullptr);
//     int t;
//     cin >> t;
//     while (t--) {
//         int n, k, res;
//         ll l;
//         char c;
//         string s;
//         cin >> n;
//         vector<int> arr(n);
//         for (int i = 0; i < n; ++i) cin >> arr[i];

//         cout << res << endl;
//     }
//     return 0;
// }


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
        nums = vector<valueType> (len + 1, 0);
        sums = vector<valueType> (len + 1, 0);
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
};


// Disjoint Set
template<typename valueType>
class DJS {
private:
    vector<valueType> arr;
    vector<valueType> rank;

public:
    DJS(valueType len) {
        arr = vector<valueType> (len);
        for (int i = 0; i < len; ++i) arr[i] = i;
        rank = vector<valueType> (len, 1);
    }

    valueType Find(valueType x) {
        if (arr[x] != x)
            arr[x] = find(arr[x]);
        return arr[x];
    }

    valueType Union(valueType x, valueType y) {
        valueType xp = find(x);
        valueType yp = find(y);
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


// Segment Tree   
template<typename valueType>     
struct Segment_TreeNode {
    int lo, hi;
    valueType sum, min, max;
    Segment_TreeNode(int lo, int hi, valueType s, valueType mi, valueType ma): lo(lo), hi(hi), sum(s), min(mi), max(ma) {};
};

template<typename valueType>         
class Segment_Tree {
private:
    vector< Segment_TreeNode<valueType>* > nodes;
    vector<bool> lazy;
    int n;
    vector<valueType> arr;

    void build(int ind, int lo, int hi) {
        if (lo == hi) {
            valueType val = arr[lo];
            nodes[ind] = new Segment_TreeNode<valueType> (lo, hi, val, val, val);
            return;
        }
        int mid = (lo + hi) / 2;
        int left = (ind << 1) + 1;
        int right = (ind << 1) + 2;

        build(left, lo, mid);
        build(right, mid + 1, hi);

        valueType nSum, nMin, nMax;
        nSum = nodes[left]->sum + nodes[right]->sum;
        nMin = min(nodes[left]->min, nodes[right]->min);
        nMax = max(nodes[left]->max, nodes[right]->max);
        
        nodes[ind] = new Segment_TreeNode<valueType> (lo, hi, nSum, nMin, nMax);
    }
    void push_up(int ind) {
        nodes[ind]->sum = nodes[(ind << 1) + 1]->sum + nodes[(ind << 1) + 2]->sum;
        nodes[ind]->min = min(nodes[(ind << 1) + 1]->min, nodes[(ind << 1) + 2]->min);
        nodes[ind]->max = max(nodes[(ind << 1) + 1]->max, nodes[(ind << 1) + 2]->max);
    }
    void push_down(int ind) {
        if (!lazy[ind]) return;
        nodes[(ind << 1) + 1]->sum = nodes[ind]->max * (nodes[(ind << 1) + 1]->hi - nodes[(ind << 1) + 1]->lo + 1);
        nodes[(ind << 1) + 1]->max = nodes[ind]->max;
        nodes[(ind << 1) + 1]->min = nodes[ind]->min;
        
        nodes[(ind << 1) + 2]->sum = nodes[ind]->max * (nodes[(ind << 1) + 2]->hi - nodes[(ind << 1) + 2]->lo + 1);
        nodes[(ind << 1) + 2]->max = nodes[ind]->max;
        nodes[(ind << 1) + 2]->min = nodes[ind]->min;
        
        lazy[ind] = false;
        lazy[(ind << 1) + 1] = true;
        lazy[(ind << 1) + 2] = true;
    }
    void _update(int ind,int l,int r,valueType val) {
        int lo = nodes[ind]->lo;
        int hi = nodes[ind]->hi;
        if (r < lo || l > hi) return ;
        if (l <= lo && r >= hi) {
            nodes[ind]->sum = val * (hi - lo + 1);
            nodes[ind]->min = val;
            nodes[ind]->max = val;
            lazy[ind] = true;
        } else {
            push_down(ind);
            _update((ind << 1) + 1, l, r, val);
            _update((ind << 1) + 2, l, r, val);
            push_up(ind);
        }
    }
public:
    Segment_Tree(int num) {
        n = num;
        nodes.resize(4*n);
        lazy.resize(4*n);
        arr.resize(n, 0);
        build(0, 0, n - 1);
    }
    Segment_Tree(vector<valueType> _arr) {
        n = _arr.size();
        nodes.resize(4*n);
        lazy.resize(4*n);
        arr = _arr;
        build(0, 0, n - 1);
    }

    void update(int l,int r,valueType val) {
        _update(0, l, r, val);
    }

    tuple<valueType, valueType, valueType> _query(int ind,int l,int r) {
        int lo = nodes[ind]->lo;
        int hi = nodes[ind]->hi;
        if (r < lo || l > hi)
            return make_tuple(0, numeric_limits<valueType>::max(), numeric_limits<valueType>::min());
        if (l <= lo && r >= hi)
            return make_tuple(nodes[ind]->sum, nodes[ind]->min, nodes[ind]->max);
            
        push_down(ind);

        valueType s1, mi1, ma1, s2, mi2, ma2, s, mi, ma;
        tie(s1, mi1, ma1) = _query((ind << 1) + 1, l, r);
        tie(s2, mi2, ma2) = _query((ind << 1) + 2, l, r);
        
        s = s1 + s2;
        mi = min(mi1, mi2);
        ma = max(ma1, ma2);
            
        return make_tuple(s, mi, ma);
    }
    int myquery(int tar,int  ind=0) {
        int lo = nodes[ind]->lo;
        int hi = nodes[ind]->hi;
        if (nodes[ind]->min > tar) return -1;
        else if (lo == hi) return lo;
        push_down(ind);
        int tmp = myquery(tar, (ind << 1) + 1);
        if (tmp == -1)
            tmp = myquery(tar, (ind << 1) + 2);
        return tmp;
    }

    valueType query_max(int l,int r) {return get<2>(_query(0, l, r));}
    valueType query_min(int l,int r) {return get<1>(_query(0, l, r));}
    valueType query_sum(int l,int r) {return get<0>(_query(0, l, r));}

};