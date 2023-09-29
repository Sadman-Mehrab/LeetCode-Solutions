class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = max(nums)
        currSum = 0
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            if currSum > maxSum:
                maxSum = currSum
        return maxSum