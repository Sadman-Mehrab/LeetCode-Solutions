class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = 0;
    int fast = 0;
    while(true){
        slow = nums[slow];
        fast = nums[fast];
        fast = nums[fast];
        if(fast == slow) break;
    }
    int newSlow = 0;
    while(true){
        slow = nums[slow];
        newSlow = nums[newSlow];
        if(slow == newSlow) break;
    }
        return slow;
    }
};