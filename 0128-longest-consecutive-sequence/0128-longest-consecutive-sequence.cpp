class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        map<int,bool> mp;
        int ans = 0;
        for(int x: nums) mp[x] = true;
        for(int x: nums) {
            if(!mp.count(x-1)){
                int len = 0;
                while(mp.count(len+x)) len++;
                ans = max(ans,len);
            }
        }
        return ans;


    }
};