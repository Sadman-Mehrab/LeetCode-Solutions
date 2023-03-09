class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}
        for c in s:
            a[c] = 0
        for c in t:
            b[c] = 0
        for c in s:
            a[c] += 1
        for c in t:
            b[c] += 1
        return a == b
            
        