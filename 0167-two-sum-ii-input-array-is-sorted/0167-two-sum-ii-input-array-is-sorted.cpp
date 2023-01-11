#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size()-1;
        vector<int> index;
        while(l<r){
            int temp = numbers[l] + numbers[r];
            if(temp == target) {
                index.push_back(l+1);
                index.push_back(r+1);
                break;
            }
            else if(temp < target) l++;
            else if(temp > target) r--;
        }
        return index;
    }
};