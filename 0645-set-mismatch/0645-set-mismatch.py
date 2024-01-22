class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numSet = set()
        dupe = total = 0
        for n in nums:
            if n in numSet:
                dupe = n
            else:
                total += n
                numSet.add(n)
        n = len(nums)
        missing = (n*(n+1)//2) - total
        return [dupe, missing]