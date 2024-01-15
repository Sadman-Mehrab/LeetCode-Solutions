class Solution:
    def repeatedCharacter(self, s: str) -> str:
        l = {}
        for c in s:
            if c not in l:
                l[c] = 1
            else:
                l[c] += 1
                if l[c] == 2:
                    return c
        