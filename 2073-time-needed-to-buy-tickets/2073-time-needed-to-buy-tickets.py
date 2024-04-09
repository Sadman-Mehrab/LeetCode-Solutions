class Solution:
    def timeRequiredToBuy(self, tickets, k: int) -> int:
        totalTime = 0 
        n = len(tickets)
        i = 0
        while tickets[k] != 0:
            if tickets[i] > 0:
                tickets[i] -= 1
                totalTime += 1
            i = (i + 1) % n                
        return totalTime
    