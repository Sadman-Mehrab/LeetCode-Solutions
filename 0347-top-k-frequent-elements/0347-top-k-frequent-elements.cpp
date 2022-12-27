class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int,int> els;
        for(int x: nums){
            els[x]++;
        }
        vector<pair<int,int>> freqs;
        for(auto x: els){
            freqs.push_back({x.second,x.first});
        }
        sort(freqs.rbegin(),freqs.rend());
        vector<int> ret;
        for(int i=0;i<k;i++){
            ret.push_back(freqs[i].second);
        }
        return ret;
    }
};