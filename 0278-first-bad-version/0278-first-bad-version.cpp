// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        return !isBadVersion(n) ? n+1 : firstBadVersion(n-1);
    }
};