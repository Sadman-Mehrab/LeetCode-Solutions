class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        c = bank[0].count('1')
        for i in range(1,len(bank)):
            r = bank[i].count('1')
            if r == 0:
                continue
            else:
                ans += c*r
                c = r
        return ans
        

