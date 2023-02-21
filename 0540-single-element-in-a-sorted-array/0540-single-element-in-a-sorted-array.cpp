
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        long long sum = 0;
        for(int x: nums) sum ^= x;
        return sum;
    }
};