class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
            if freq[n] > l/2:
                return n
        return 0
        
        