class Solution {
public:
    int climbStairs(int n) {
        int a = 1, b = 1;
        n--;
        while(n--){
            int t = a;
            a += b;
            b = t;
        }
            

        return a;
    }
};