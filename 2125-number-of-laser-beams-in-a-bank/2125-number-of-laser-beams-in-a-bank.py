class Solution:
    def countOne(self, row):
        c = 0
        for r in row:
            if r == '1':
                c += 1
        return c

    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        c = self.countOne(bank[0])
        
        for i in range(1, len(bank)):
            r = self.countOne(bank[i])
            if r == 0:
                continue
            else:
                ans += r*c 
                c = r

        return ans
            

