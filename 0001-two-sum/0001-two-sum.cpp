class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector <int> res;
        map<int,int> nums2;
        for(int i=0;i<nums.size();i++){
            if(nums2.count(target-nums[i])){
                res.push_back(i);
                res.push_back(nums2[target-nums[i]]);
                break;
            }
            nums2[nums[i]] = i;
        }
        return res;
    }
};