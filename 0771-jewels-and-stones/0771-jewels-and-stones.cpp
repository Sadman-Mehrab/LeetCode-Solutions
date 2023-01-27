#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool found(string s, char  x){
        for(char c: s) if(x == c) return true;
        return false;
    }
    int numJewelsInStones(string jewels, string stones) {
        int c = 0;
        for(char x: stones) if(found(jewels,x)) c++;
        return c;
    }
};