class Solution {
public:
    string frequencySort(string s) {
        map<char,int > freq;
        string ret;
        vector<pair<int,char>> rev;
        for(char x: s) freq[x]++;
        for(auto x: freq) rev.push_back({x.second,x.first});
        sort(rev.rbegin(),rev.rend());
        for(auto x: rev) for(int i=0;i<x.first;i++) ret.push_back(x.second);    
        return ret;
    }
};