class Solution {
public:
    bool isSubsequence(string s, string t) {
        if(s == t) return true;
        int j=0,k=0;
        while(j<t.length()){
            if(t[j] == s[k]){
                k++;
            }
            if(k == s.length()) return true;
            j++;
        }
        return false;
    }
};