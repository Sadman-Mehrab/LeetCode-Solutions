#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool isPalindrome(string s) {
        string x = "";
        for(char c : s)
            if((c>=97 && c<=122)||(c>=65 && c<=90)||(c>=48 && c<=57))
                x += tolower(c);
        
        s = x;
        reverse(s.begin(),s.end());
        return s == x;

    }
};