class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {

        sort(people.begin(),people.end());
        int l = 0, r = people.size()-1, c = 0;
        while(l<=r){
            r--;
            if(people[l] <= (limit - people[r+1]) && l<=r) l++;
            c++;
        }
        return c;
    }
};