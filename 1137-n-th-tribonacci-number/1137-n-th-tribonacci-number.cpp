#include <bits/stdc++.h>
using namespace std;

class Solution {
private:
    int dp[40];
public:
    int tribonacci(int n) {
        if(n <= 1) return n;
        else if(n == 2) return n-1;
        else if(dp[n] != 0) return dp[n];
        else return dp[n] = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3);
    }
};