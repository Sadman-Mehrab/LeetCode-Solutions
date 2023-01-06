#include<bits/stdc++.h>
using namespace std;

class Solution {
public:

    bool isSubstring(string a, string b){
        int j = 0;
        for(int i=0;i<a.length();i++){
            if(a[i] == b[j] && j == b.length()-1 ) return true;
            if(a[i] == b[j]) j++;
        }
        return false;
    }

    bool canConstruct(string ransomNote, string magazine) {
        sort(ransomNote.begin(),ransomNote.end());
        sort(magazine.begin(),magazine.end());
        return isSubstring(magazine,ransomNote);
    }
};