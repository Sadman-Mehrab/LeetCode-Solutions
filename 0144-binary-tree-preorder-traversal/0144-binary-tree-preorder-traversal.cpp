/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void traverse(vector<int> &list ,TreeNode * temp){
        if(temp == NULL) return;
        list.push_back(temp->val);
        traverse(list,temp->left);
        traverse(list,temp->right);
    }
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> list;
        traverse(list,root);
        
        return list;
    }
};