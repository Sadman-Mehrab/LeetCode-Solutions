class Solution {
public:
    int singleNumber(vector<int>& nums) {
        long long s = 0;
        for(int x: nums) s^=x;
        return s;
    }
};