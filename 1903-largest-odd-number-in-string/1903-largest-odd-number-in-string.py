class Solution:
    def largestOddNumber(self, num: str) -> str:
        largeNumSTR = ""
        largeNum = ""
        for c in num:
            largeNumSTR += c
            if int(c)%2 == 1:
                largeNum = largeNumSTR
        return largeNum
            
        
