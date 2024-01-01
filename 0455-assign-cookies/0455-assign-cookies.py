class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        c = 0 
        for n in g:
            for i in range(len(s)):
                if s[i] >= n:
                    s[i] = -1
                    c += 1
                    break

        return c 
