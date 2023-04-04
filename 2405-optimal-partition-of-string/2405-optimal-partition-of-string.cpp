class Solution {
public:
    int partitionString(string s) {
        int c = 1;
        map<char,bool> mp;
        for(char x: s){
            if(mp.count(x)){
                c++;
                mp.clear();
            }
            mp[x] = true;
                
        }
        return c;
    }
};