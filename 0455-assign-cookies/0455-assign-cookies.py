class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        c = 0 
        lastCookie = -1
        for n in g:
            for i in range(lastCookie+1,len(s)):
                if s[i] >= n:
                    s[i] = -1
                    c += 1
                    lastCookie = i
                    break

        return c 
