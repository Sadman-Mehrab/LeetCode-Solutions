class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        long long maxSum = INT_MIN;
        long long curr = 0;
        for(int i=0;i<nums.size();i++){
            curr += nums[i];
            if (curr > maxSum) maxSum = curr;
            if(curr < 0) curr = 0;
        }
        return maxSum;
    }
};