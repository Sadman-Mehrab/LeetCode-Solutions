class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = sorted(heights)
        count = 0
        n = len(heights)
        for i in range(n):
            if sortedHeights[i] != heights[i]:
                count += 1
        return count
            