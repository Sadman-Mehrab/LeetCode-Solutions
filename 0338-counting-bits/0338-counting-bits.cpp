class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> bits;
        for(int i=0;i<=n;i++){
            int k = i;
            int c = 0;
            while(k>0){
                if(k&1) c++;
                k>>=1;
            }
            bits.push_back(c);
        }
        return bits;
    }
};