class Solution:
    def signFunc(self, x):
        if x == 0:
            return 0
        elif x > 0:
            return 1
        else:
            return -1
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for n in nums:
            prod *= n
        return self.signFunc(prod)