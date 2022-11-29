class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        for(int i=0;i<=n;i++){
            nums.push_back(i);
        }
        int sum = 0;
        for(int x: nums) sum ^= x;
        return sum;
    }
};