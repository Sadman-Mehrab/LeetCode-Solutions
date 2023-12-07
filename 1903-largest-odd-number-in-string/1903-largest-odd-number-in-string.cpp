#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string largestOddNumber(string num) {
        string largeNumSTR = "";
        string largeNum = "";
        for (char x: num){
            largeNumSTR += x;
            if((x - 48)%2 == 1 ){
                largeNum = largeNumSTR;
            }
        }        
        return largeNum;
    }
};