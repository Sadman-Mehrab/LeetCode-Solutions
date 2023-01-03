#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isSorted(string s){
        for(int i=0;i<s.length()-1;i++){
            if(s[i+1]<s[i]) return false;
        }
        return true;
        

    }
    
    int minDeletionSize(vector<string>& strs) {
        int c = 0;
        for(int i=0;i<strs[0].length();i++){
            string temp = "";
            for(string s: strs) temp += s[i];
            if(!isSorted(temp)) c++;
        }

        return c;
    }
        
};