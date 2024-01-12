class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        n = len(s)
        a = s[:(n//2)]
        b = s[(n//2):]
        ans = 0
        for c in a:
            if c in v:
                ans += 1
        for c in b:
            if c in v:
                ans -= 1
        
        return ans == 0