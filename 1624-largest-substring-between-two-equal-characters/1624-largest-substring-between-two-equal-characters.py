class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        idx = {}
        result = -1

        for i in range(len(s)):
            if s[i] in idx:
                l = i - idx[s[i]] - 1
                if l > result:
                    result = l
            else:
                idx[s[i]] = i

        return result
