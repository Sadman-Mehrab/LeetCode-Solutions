class Solution:
    def balancedStringSplit(self, s: str) -> int:
        mp = {}
        res = 0
        for c in s:
            if c not in mp:
                mp[c] = 1
            else:
                mp[c] += 1
            if 'L' in mp and 'R' in mp:
                if mp['L'] == mp['R']:
                    res += 1 
                    mp = {}
        return res