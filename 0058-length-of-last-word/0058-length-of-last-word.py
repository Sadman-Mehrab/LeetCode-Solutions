class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        seenSpace = False
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ': seenSpace = True
            if s[i] != ' ': count += 1
            if s[i] == ' ' and seenSpace and count != 0: break
        return count