class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        all = set()
        losers = defaultdict(int)
        ans1, ans2 = [], []

        for m in matches:
            all.add(m[0])
            all.add(m[1])
            losers[m[1]] += 1
            
        for k in losers:
            if losers[k] == 1:
                ans2.append(k)
        
        for a in all:
            if a not in losers:
                ans1.append(a)

        return [sorted(ans1), sorted(ans2)]
    


