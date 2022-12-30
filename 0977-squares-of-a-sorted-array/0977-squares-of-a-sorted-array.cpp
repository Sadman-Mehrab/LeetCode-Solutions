class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int l = 0;
        int r = nums.size()-1;
        int k = r;
        vector<int> ret(nums.size());
        while(k>=0){
            if(nums[l]*nums[l] > nums[r]*nums[r]){
                ret[k--] = nums[l]*nums[l];
                l++;
            }
            else{
                ret[k--] = nums[r]*nums[r];
                r--;
            }
        }
        return ret;
    }
};
