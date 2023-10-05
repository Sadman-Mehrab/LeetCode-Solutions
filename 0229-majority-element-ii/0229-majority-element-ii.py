# boyer-moore majority voting algorithm    
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2, f1, f2 = 0, 0, 0, 0

        for n in nums:
            if f1 == 0 and n != c2:
                c1 = n
                f1 = 1
            elif f2 == 0 and n != c1:
                c2 = n
                f2 = 1
            elif n == c1:
                f1 += 1
            elif n == c2:
                f2 += 1
            else:
                f1 -= 1
                f2 -= 1

        f1, f2 = 0, 0

        for n in nums:
            if n == c1:
                f1 += 1
            elif n == c2:
                f2 += 1

        ret = []

        if f1 > len(nums)//3:
            ret.append(c1)
        if f2 > len(nums)//3:
            ret.append(c2)
        return ret 

            
                

            