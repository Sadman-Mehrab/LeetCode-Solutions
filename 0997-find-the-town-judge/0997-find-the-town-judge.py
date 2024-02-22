class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        mp = {}
        # mp[person] : [trusts, trustedBy]
        for t in trust:
            x, y = t

            if x not in mp:
                mp[x] = [0, 0]
            if y not in mp:
                mp[y] = [0, 0]

            mp[x][0] += 1
            mp[y][1] += 1

        for k in mp:
            if mp[k][0] == 0 and mp[k][1] == (n - 1):
                return k
        
        return -1
    
