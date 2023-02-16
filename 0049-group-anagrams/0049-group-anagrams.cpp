#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    map <char, int> groupKey(string s){
        map<char, int> res;
        for(char x: s) res[x]++;
        return res;
    }
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<map <char, int>,vector<string>> groups;
        vector<vector<string>> result;
        for(string s: strs)
            groups[groupKey(s)].push_back(s);
        for(auto x: groups)
            result.push_back(x.second);
        return result;
    }
};