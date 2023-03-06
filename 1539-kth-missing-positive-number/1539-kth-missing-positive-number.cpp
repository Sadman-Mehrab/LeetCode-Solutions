class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        map<int,bool> present;
        vector<int> missing;
        for(int x: arr) present[x] = true;
        for(int i=1;missing.size() < k;i++) if(!present[i]) missing.push_back(i);
        return missing[k-1];
    }
};