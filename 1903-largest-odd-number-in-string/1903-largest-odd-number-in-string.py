class Solution:
    def largestOddNumber(self, num: str) -> str:
        idx = 0 
        for i in range(len(num)):
            if int(num[i]) % 2 == 1:
                idx = i
        if idx == 0 and int(num[idx]) % 2 == 1:
            return num[idx]
        elif idx == 0:
            return ""
        else:
            return num[:idx+1]
        
        
