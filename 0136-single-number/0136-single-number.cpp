class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int s = 0;
        for(int x: nums) s^=x;
        return s;
    }
};