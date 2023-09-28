class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mp = {}
        for c in "balloon":
            mp[c] = 0
        for c in text:
            if c in mp:
                mp[c] += 1
        mp['l'] //= 2
        mp['o'] //= 2

        return min(mp.values())