#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> scores;
        int ans = 0;
        for(string x: operations){
            if(x == "+"){
                int a = scores.top();
                scores.pop();
                int b = scores.top();
                scores.push(a);
                scores.push(a+b);
                ans += (a+b);
            }
            else if(x == "D"){
                int a = scores.top();
                scores.push(2*a);
                ans += (2*a);
            }
            else if(x == "C"){
                int a = scores.top();
                scores.pop();
                ans -= a;
            }
            else{
                scores.push(stoi(x));
                ans += stoi(x);
            }

        }

        return ans;
    } 
};