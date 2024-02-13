class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if self.isPalindrome(w):
                return w
        return ""
        
