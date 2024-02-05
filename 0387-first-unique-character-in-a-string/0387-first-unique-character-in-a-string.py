class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = []
            freq[s[i]].append(i)
        for c in s:
            if len(freq[c]) == 1:
                return freq[c][0]
        return -1