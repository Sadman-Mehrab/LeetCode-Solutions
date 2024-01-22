class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dupe = 0
        sum = 0
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        for k in freq:
            if freq[k] == 2:
                dupe = k
            sum += k
        n = len(nums)
        missing = (n*(n+1)//2) - sum
        return [dupe, missing]