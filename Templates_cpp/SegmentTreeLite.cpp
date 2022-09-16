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

#define MX 1
// #define MN 1
// #define SM 1

using namespace std;


// Segment Tree   
template<typename valueType>     
struct Segment_TreeNode {
    int lo, hi;
#ifdef SM
    valueType sum = 0;
#elif MN
    valueType min = 0;
#elif MX
    valueType max = 0;
#endif
    Segment_TreeNode(int lo, int hi, valueType tmp): lo(lo), hi(hi) {
#ifdef SM
        sum = tmp;
#elif MN
        min = tmp;
#elif MX
        max = tmp;
#endif
    };
    Segment_TreeNode(int lo, int hi): lo(lo), hi(hi) {};
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
            nodes[ind] = new Segment_TreeNode<valueType> (lo, hi, arr[lo]);
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
#ifdef SM
        nodes[ind]->sum = nodes[left]->sum + nodes[right]->sum;
#elif MN
        nodes[ind]->min = min(nodes[left]->min, nodes[right]->min);
#elif MX
        nodes[ind]->max = max(nodes[left]->max, nodes[right]->max);
#endif
    }

    void push_down(int ind) {
        if (!lazy[ind]) return;
        int left = (ind << 1) + 1;
        int right = (ind << 1) + 2;
#ifdef SM
        nodes[left]->sum = nodes[ind]->max * (nodes[left]->hi - nodes[left]->lo + 1);
#elif MN
        nodes[left]->min = nodes[ind]->min;
#elif MX
        nodes[left]->max = nodes[ind]->max;
#endif
#ifdef SM
        nodes[right]->sum = nodes[ind]->max * (nodes[right]->hi - nodes[right]->lo + 1);
#elif MN        
        nodes[right]->min = nodes[ind]->min;
#elif MX
        nodes[right]->max = nodes[ind]->max;
#endif    
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
#ifdef SM
            nodes[ind]->sum = val * (hi - lo + 1);
#elif MN  
            nodes[ind]->min = val;
#elif MX
            nodes[ind]->max = val;
#endif 
            lazy[ind] = true;
        } else {
            push_down(ind);
            _update(left, l, r, val);
            _update(right, l, r, val);
            push_up(ind);
        }
    }

    valueType _query(int ind, int l, int r) {
        int lo = nodes[ind]->lo;
        int hi = nodes[ind]->hi;
        int left = (ind << 1) + 1;
        int right = (ind << 1) + 2;

        if (r < lo || l > hi)
#ifdef SM
            return 0;
#elif MN
            return numeric_limits<valueType>::max();
#elif MX
            return numeric_limits<valueType>::min();
#endif
        if (l <= lo && r >= hi)
#ifdef SM
            return nodes[ind]->sum;
#elif MN
            return nodes[ind]->min,;
#elif MX
            return  nodes[ind]->max;
#endif
            
        push_down(ind);

        valueType tmp1, tmp2 ;
        tmp1 = _query(left, l, r);
        tmp2 = _query(right, l, r);
#ifdef SM
        return tmp1 + s2;
#elif MN
        return min(tmp1, tmp2);
#elif MX
        return max(tmp1, tmp2);
#endif
    }
public:

    Segment_Tree(valueType num) {
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

    void update(int l, int r, valueType val) {_update(0, l, r, val);}
    void update(int l, valueType val) {_update(0, l, l, val);}
    valueType query(int l, int r) {return (_query(0, l, r));}

};