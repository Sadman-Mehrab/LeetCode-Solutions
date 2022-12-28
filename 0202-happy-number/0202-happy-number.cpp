#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isHappy(int n) {
        map <int,int> nums;
        nums[n]++;
        long long a = (long long ) n;
        while(true){
            long long num = 0;
            string temp = to_string(a);
            for(char x: temp) num += ((x-48)*(x-48));
            if(nums.count(num) && num == 1) return true;
            if(nums.count(num) && num != 1) return false;
            nums[num]++;
            a = num;
        }
    }
};