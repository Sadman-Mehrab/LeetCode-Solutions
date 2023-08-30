class Solution:
    def isAlpha(self, c):
        return ((ord('A') <= ord(c) and ord(c) <= ord('Z')) or
                (ord('a') <= ord(c) and ord(c) <= ord('z')) or
                (ord('0') <= ord(c) and ord(c) <= ord('9'))
                )

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l <= r:
            if not self.isAlpha(s[l]):
                l += 1
                continue
            if not self.isAlpha(s[r]):
                r -= 1
                continue
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
            
        return True
