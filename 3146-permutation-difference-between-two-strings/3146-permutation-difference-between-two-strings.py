from collections import defaultdict
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        mp1, mp2 = {}, {}
        for i in range(len(s)):
            mp1[s[i]] = i
        
        for i in range(len(t)):
            mp2[t[i]] = i
            
        ans = 0
        
        for c in s:
            ans += abs(mp1[c] - mp2[c])
        
        return ans
        