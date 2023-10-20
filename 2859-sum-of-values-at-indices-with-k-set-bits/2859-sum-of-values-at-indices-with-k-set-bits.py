class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            c, j = 0, i
            while j > 0:
                if j & 1:
                    c += 1
                j >>= 1
            if c == k:
                res += nums[i]
        return res


