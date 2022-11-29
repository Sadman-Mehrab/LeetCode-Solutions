#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int,int> seen;
        for(int i=0;i<nums.size();i++){
            if(seen.count(nums[i]) && abs(i - seen[nums[i]]) <= k) {
                return true;
            }
            seen[nums[i]] = i;
        }
        return false;
    }
};