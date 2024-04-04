class Solution:
    def maxDepth(self, s: str) -> int:
        balance = 0
        maxBalance = 0
        for c in s:
            maxBalance = max(balance, maxBalance)
            if c == '(':
                balance += 1
            elif c == ')':
                balance -= 1
        return maxBalance                
        
        


