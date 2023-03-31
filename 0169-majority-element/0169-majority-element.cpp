class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int major = 0;
        map<int, int> freq;
        for(int x: nums){
            freq[x]++;
            if(freq[x] > (nums.size()/2)) major = x;
            
        }
        return major;
    }
};