#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string frequencySort(string s) {
        map<char,int > freq;
        for(char x: s) freq[x]++;
        vector<pair<int,char>> rev;
        for(auto x: freq){
            rev.push_back({x.second,x.first});
        }
        string ret;
        sort(rev.rbegin(),rev.rend());
        for(auto x: rev){
            int y = x.first;
            while(y--){
                ret.push_back(x.second);
            }
        }   
        return ret;
    }
};
