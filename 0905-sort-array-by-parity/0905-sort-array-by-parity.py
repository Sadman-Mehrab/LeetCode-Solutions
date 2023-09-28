class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ev = []
        od = []
        for n in nums:
            if n&1:
                od.append(n)
            else:
                ev.append(n)
        return ev+od