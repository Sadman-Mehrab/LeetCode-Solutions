class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, k = 0 , len(nums) - 1, len(nums) - 1 
        ans = [0]*len(nums)
        while k >= 0:
            if nums[r]**2 > nums[l]**2:
                ans[k] = nums[r]**2
                k -= 1
                r -= 1
            else:
                ans[k] = nums[l]**2
                k -= 1
                l += 1

        return ans
            
            