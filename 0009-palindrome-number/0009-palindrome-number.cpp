class Solution {
public:
    bool isPalindrome(int x) {
        string s = std::to_string(x);
        string p = s;
        std::reverse(p.begin(),p.end());
        return p == s ? true : false;
    }
};