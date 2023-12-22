#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxScore(string s) {
        int ans = 0;

        for(int i=0;i<s.length()-1;i++){
            int mx = 0;
            for(int j=0;j<=i;j++) if(s[j] == '0') mx++;
            for(int j=i+1;j<s.length();j++) if(s[j] == '1') mx++;
            if (mx > ans) ans = mx;
        }
            
        return ans;
    }

};

