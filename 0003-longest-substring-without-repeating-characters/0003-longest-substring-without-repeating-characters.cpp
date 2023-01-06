class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        int maxLen = 0;
        for(int i=0;i<n;i++){
            int currLen = 0;
            map<char,int> sub;
            for(int j=i;j<n;j++){
                if(sub.count(s[j])) break;
                else sub[s[j]]++;
                currLen++;
                maxLen = max(currLen,maxLen);
            }
        }
        return maxLen;
    }
};
