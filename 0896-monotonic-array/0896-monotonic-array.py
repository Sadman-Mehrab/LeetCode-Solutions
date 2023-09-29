class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True

        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                inc = False
                break
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                dec = False
                break

        return inc or dec
