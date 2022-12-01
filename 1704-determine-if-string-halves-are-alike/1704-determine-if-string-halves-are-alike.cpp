#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int getCount(string s){
        int c = 0;
        for(char x: s){
            if(
                x == 'o' ||
                x == 'O' ||
                x == 'a' ||
                x == 'A' ||
                x == 'i' ||
                x == 'I' ||
                x == 'e' ||
                x == 'E' ||
                x == 'u' ||
                x == 'U'
            ) c++;
        }
         return c;       
    }
    bool halvesAreAlike(string s) {
        string a,b;
        for(int i=0;i<s.length()/2;i++) a.push_back(s[i]);
        for(int i=s.length()/2;i<s.length();i++) b.push_back(s[i]);
        return getCount(a) == getCount(b);
    }
};