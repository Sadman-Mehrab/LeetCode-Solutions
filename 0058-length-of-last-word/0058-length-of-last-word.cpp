class Solution {
public:
    int lengthOfLastWord(string s) {
        int c = 0;
        bool seenSpace = false;
        for(int i=s.length()-1;i>=0;i--){
            if(s[i] == ' ') seenSpace = true;
            if(s[i]!=' ') c++;
            if(seenSpace && s[i]==' ' && c!=0) break;
        }
        return c;
    }
};