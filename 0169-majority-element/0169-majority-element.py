class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        freq = Counter(nums)
        for f in freq:
            if freq[f] > l/2:
                return f
        return 0
        
        