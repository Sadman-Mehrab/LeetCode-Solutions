class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            freq[n] = 0
        for n in nums:
            freq[n] += 1
            if freq[n] > len(nums)/2:
                return n
        return 0
        
        