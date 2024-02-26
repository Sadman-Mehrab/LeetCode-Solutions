import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatingTimePossible(piles, time, hour):
            total = 0
            for p in piles:
                total += math.ceil(p/time)
            return hour >= total
        
        l, r = 1, max(piles)
        while l < r:
            m = l + (r - l)//2
            if eatingTimePossible(piles,m,h):
                r = m
            else:
                l = m + 1
        
        return l
