class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        vector<int> res;
        sort(potions.begin(),potions.end());
        for(int x: spells){
            int leftIndex = -1;
            int l = 0,r = potions.size()-1;
            while(l<=r){
                int m = l + (r-l)/2;
                long long prod = (long long) potions[m]*x;
                if(prod >= success){
                    r = m - 1;
                    leftIndex = m;

                }
                else{
                    l = m + 1;
                }
            }
            if(leftIndex == -1) res.push_back(0);
            else res.push_back(potions.size()-leftIndex);
        }
        return res;
    }
};