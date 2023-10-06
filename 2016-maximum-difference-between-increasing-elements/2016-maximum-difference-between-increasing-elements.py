class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        i = 0
        maxDifference = -1
        for j in range(1,len(nums)):
            if nums[j] > nums[i]:
                maxDifference = max(maxDifference, nums[j] - nums[i])
            else:
                i = j
        return maxDifference