// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        while(true){
            if(!isBadVersion(n)) return n+1;
            n--;
        }
        return -1;
    }
};