class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def genPar(t, l, r, s):
            if t == l and t == r:
                res.append(s)
                return
            if l < t:
                genPar(t, l + 1, r, s + '(')
            if r < l:
                genPar(t, l, r + 1, s + ')')
        genPar(n, 0, 0, '')
        return res