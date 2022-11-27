#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <unordered_map>


using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

TreeNode* Build(vector<int>& postOrd, int postStart, int postEnd, vector<int>& inOrd, int inStart, int inEnd, unordered_map<int,int>& mp) {
    if (postStart > postEnd || inStart > inEnd) return nullptr;
    TreeNode* root = new TreeNode(postOrd[postEnd]);
    int inRoot = mp[root->val];
    int numsLeft = inRoot - inStart;
    
    root->left = Build(postOrd, postStart, postStart + numsLeft - 1, inOrd, inStart, inRoot - 1, mp);
    root->right = Build(postOrd, postStart + numsLeft, postEnd - 1, inOrd, inRoot + 1, inEnd, mp);
    return root;
}

void getPreorder(TreeNode* root, vector<int>& preOrd) {
    if (!root) return;
    preOrd.push_back(root->val);
    getPreorder(root->left, preOrd);
    getPreorder(root->right, preOrd);
    return;
}

int main() {
    cout.sync_with_stdio(false);
    cin.tie(nullptr);

    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> postOrd(n), inOrd(n), preOrd, mxVals;
        for (int i = 0; i < n; ++ i) cin >> postOrd[i];

        // inorder 
        for (int i = 0; i < n; ++ i) inOrd[i] = postOrd[i];
        sort(inOrd.begin(), inOrd.end());
        
        // map to find the index in inorder
        unordered_map<int, int> inOrdMap;
        for(int i = 0; i < n; i++) inOrdMap[inOrd[i]] = i;

        // Build Tree
        TreeNode* root = Build(postOrd, 0, n - 1, inOrd, 0, n - 1, inOrdMap);
        
        // preorder
        getPreorder(root, preOrd);

        // max values for each level
        vector<TreeNode*> que;
        que.push_back(root);
        while (!que.empty()) {
            vector<TreeNode*> nxt_que;
            int mx = -1005;
            for (TreeNode* nd: que) {
                mx = max(mx, nd->val);
                if (nd->left) nxt_que.push_back(nd->left);
                if (nd->right) nxt_que.push_back(nd->right);
            }
            mxVals.push_back(mx);
            que = nxt_que;
        }

        // output
        for (int v: preOrd) cout << v << ' ';
        cout << endl << mxVals.size() << endl;
        for (int v: mxVals) cout << v << endl;
    }
    return 0;
}