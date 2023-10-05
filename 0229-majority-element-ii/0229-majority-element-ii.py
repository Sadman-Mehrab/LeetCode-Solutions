class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mp = {}
        ret = []
        for i in nums:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1
        for key in mp:
            if mp[key] > n//3:
                ret.append(key)
        return ret