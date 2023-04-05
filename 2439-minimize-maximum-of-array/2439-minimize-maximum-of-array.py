class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = nums[0]
        tot = nums[0]
        for i in range(1,len(nums)):
            tot += nums[i]
            avg = math.ceil(tot/(i+1))
            ans = max(ans,avg)
        return ans