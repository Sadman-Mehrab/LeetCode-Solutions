#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        vector<int> temp;
        int c = nums.size();
        for(int x: nums) if(x != 0){
            temp.push_back(x);
            c--;
        }
        nums.clear();
        for(int x: temp) nums.push_back(x);
        while(c--) nums.push_back(0);
            
    }
};