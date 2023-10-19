class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss = []
        tt = []
        for c in s:
            if c != '#':
                ss.append(c)
            else:
                if len(ss) != 0:
                    ss.pop()
        
        for c in t:
            if c != '#':
                tt.append(c)
            else:
                if len(tt) != 0:
                    tt.pop()
        
        return tt == ss 
        