#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int firstUniqChar(string s) {
        map<char,int> lets;
        for(char x: s) lets[x]++;
        for(int i=0;i<s.length();i++) if(lets[s[i]] == 1) return i;
        return -1;
    }
};
