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


// Segment Tree   
template<typename valueType>     
struct Segment_TreeNode {
    int lo, hi;
    valueType sum, min, max;
    Segment_TreeNode(int lo, int hi, valueType s, valueType mi, valueType ma): lo(lo), hi(hi), sum(s), min(mi), max(ma) {};
    Segment_TreeNode(int lo, int hi): lo(lo), hi(hi), sum(0), min(0), max(0) {};
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
            nodes[ind] = new Segment_TreeNode<valueType> (lo, hi, arr[lo], arr[lo], arr[lo]);
            return;
        }
        int mid = (lo + hi) / 2;
        int left = (ind << 1) + 1;
        int right = (ind << 1) + 2;

        build(left, lo, mid);
        build(right, mid + 1, hi);

        nodes[ind] = new Segment_TreeNode<valueType> (lo, hi);
        push_up(ind);
    }

    void push_up(int ind) {
        int left = (ind << 1) + 1;
        int right = (ind << 1) + 2;

        nodes[ind]->sum = nodes[left]->sum + nodes[right]->sum;
        nodes[ind]->min = min(nodes[left]->min, nodes[right]->min);
        nodes[ind]->max = max(nodes[left]->max, nodes[right]->max);
    }

    void push_down(int ind) {
        if (!lazy[ind]) return;
        int left = (ind << 1) + 1;
        int right = (ind << 1) + 2;

        nodes[left]->sum = nodes[ind]->max * (nodes[left]->hi - nodes[left]->lo + 1);
        nodes[left]->max = nodes[ind]->max;
        nodes[left]->min = nodes[ind]->min;
        
        nodes[right]->sum = nodes[ind]->max * (nodes[right]->hi - nodes[right]->lo + 1);
        nodes[right]->max = nodes[ind]->max;
        nodes[right]->min = nodes[ind]->min;
        
        lazy[ind] = false;
        lazy[left] = true;
        lazy[right] = true;
    }

    void _update(int ind, int l ,int r, valueType val) {
        int lo = nodes[ind]->lo;
        int hi = nodes[ind]->hi;
        int left = (ind << 1) + 1;
        int right = (ind << 1) + 2;

        if (r < lo || l > hi) return ;

        if (l <= lo && r >= hi) {
            nodes[ind]->sum = val * (hi - lo + 1);
            nodes[ind]->min = val;
            nodes[ind]->max = val;
            lazy[ind] = true;
        } else {
            push_down(ind);
            _update(left, l, r, val);
            _update(right, l, r, val);
            push_up(ind);
        }
    }

    tuple<valueType, valueType, valueType> _query(int ind, int l, int r) {
        int lo = nodes[ind]->lo;
        int hi = nodes[ind]->hi;
        int left = (ind << 1) + 1;
        int right = (ind << 1) + 2;

        if (r < lo || l > hi)
            return make_tuple(0, numeric_limits<valueType>::max(), numeric_limits<valueType>::min());
        if (l <= lo && r >= hi)
            return make_tuple(nodes[ind]->sum, nodes[ind]->min, nodes[ind]->max);
            
        push_down(ind);

        valueType s1, mi1, ma1, s2, mi2, ma2;
        tie(s1, mi1, ma1) = _query(left, l, r);
        tie(s2, mi2, ma2) = _query(right, l, r);
            
        return make_tuple(s1 + s2, min(mi1, mi2), max(ma1, ma2));
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

    void update(int l,int r,valueType val) {_update(0, l, r, val);}
    void update(int l, valueType val) {_update(0, l, l, val);}
    valueType query_max(int l,int r) {return get<2>(_query(0, l, r));}
    valueType query_min(int l,int r) {return get<1>(_query(0, l, r));}
    valueType query_sum(int l,int r) {return get<0>(_query(0, l, r));}

};