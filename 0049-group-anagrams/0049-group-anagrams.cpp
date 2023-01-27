#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string getSorted(string a){
        sort(a.begin(),a.end());
        return a;
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string,vector<string>> groups;
        vector<vector<string>> result;
        for(string s: strs)
            groups[getSorted(s)].push_back(s);
        for(auto x: groups)
            result.push_back(x.second);
        return result;
    }
};