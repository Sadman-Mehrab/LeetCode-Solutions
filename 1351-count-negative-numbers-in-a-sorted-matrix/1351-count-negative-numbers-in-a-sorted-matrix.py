class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        for g in grid:
            l, r = 0, len(g) - 1
            count = 0
            if g[r] >= 0:
                continue

            while l <= r:
                m = l + (r - l)//2
                if g[m] >= 0:
                    l = m + 1
                else:
                    count += (r - m) + 1
                    r = m - 1
            total += count
        
        return total
