class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        for i in range(len(candies)):
            candies[i] += extraCandies
            if candies[i] == max(candies):
                res.append(True)
            else:
                res.append(False)
            candies[i] -= extraCandies
        return res

