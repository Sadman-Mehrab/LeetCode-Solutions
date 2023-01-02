
class Solution {
public:
    bool detectCapitalUse(string word) {
        int c = 0;
        for(char x: word)
            if(x == toupper(x)) c++;

        if(c == word.length()) return true;
        else if(c == 1 && word[0] == toupper(word[0])) return true;
        else if(c == 0) return true;
        else return false;
    }
};